from PySide2.QtWidgets import QDialog, QTreeWidgetItem, QFileDialog, QMessageBox
from PySide2.QtCore import Qt, QThread, Signal
from PySide2.QtGui import QIcon
from ui_restore_dialog import Ui_RestoreDialog
from repo import Repo, get_datetime_obj
from models import Utils, get_resource_path
from download_snapshot_thread import DownloadSnapshotThread

import os


def pretty_time(snapshot_id):
    datetime_obj = get_datetime_obj(snapshot_id)
    return datetime_obj.strftime("%b %d %Y %I:%M:%S %p")


class GetPathsThread(QThread):
    result = Signal(object)

    def __init__(self, index, snapshot_tree_widget, dirs, snapshot):
        QThread.__init__(self)
        self.index = index
        self.snapshot_tree_widget = snapshot_tree_widget
        self.dirs = dirs
        self.snapshot = snapshot

    def run(self):
        selected_paths = [
            self.index[item] for item in self.snapshot_tree_widget.findItems(
                "", Qt.MatchContains
                | Qt.MatchRecursive) if item.checkState(0) == Qt.Checked
        ]
        paths = set()
        node_paths = [node["path"] for node in self.snapshot]
        for path in node_paths:
            should_include = sum(
                1 for selected_path in selected_paths if
                (selected_path in self.dirs and f"{selected_path}/" in path) or
                (selected_path not in self.dirs and selected_path in path)) > 0
            if should_include:
                paths.add(path)
        self.result.emit(paths)


class PopulateDirsThread(QThread):
    result = Signal(object)

    def __init__(self, snapshot):
        QThread.__init__(self)
        self.snapshot = snapshot

    def run(self):
        dirs = {}
        for node in self.snapshot:
            dirname = os.path.dirname(node["path"])
            if dirname not in dirs:
                dirs[dirname] = set()
            dirs[dirname].add(node["path"])
        self.result.emit(dirs)


class RestoreDialog(QDialog, Ui_RestoreDialog):
    def __init__(self, window, backup):
        QDialog.__init__(self)
        Ui_RestoreDialog.__init__(self)

        self.setupUi(self)
        self.window = window
        self.backup = backup
        self.restore_dir = None
        self.paths = None
        self.snapshot_id = None
        self.snapshot_ids_to_str = {}

        self.populate_snapshots()

        self.snapshots_combo_box.currentTextChanged.connect(
            self.populate_snapshot)
        self.snapshot_tree_widget.itemExpanded.connect(self.item_clicked)
        self.restore_button.pressed.connect(self.restore_start)

        self.reset_tree()

    def restore_finish(self, paths, snapshot_id):
        self.status_label.clear()
        self.setEnabled(True)
        if len(paths) is 0:
            return
        restore_dir = QFileDialog.getExistingDirectory()
        if len(restore_dir) is 0:
            return

        self.restore_dir = restore_dir
        self.paths = paths
        self.snapshot_id = snapshot_id

        reply = QMessageBox.information(
            self.window, "Start Restore?",
            f"You are about to restore to {restore_dir}. Continue?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply is QMessageBox.No:
            return

        if len(os.listdir(restore_dir)) is not 0:
            reply = QMessageBox.information(
                self.window, "Potential Overwrite?",
                f"You are restoring to a non-empty folder! BlobBackup will OVERWRITE any conflicting paths. Continue?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply is QMessageBox.No:
                return

        self.accept()

    def restore_start(self):
        if self.snapshots_combo_box.count() is 0:
            return
        snapshot_id = self.snapshot_ids_to_str[
            self.snapshots_combo_box.currentText()]
        self.thread = GetPathsThread(self.index, self.snapshot_tree_widget,
                                     self.dirs, self.snapshot)
        self.thread.result.connect(
            lambda x: self.restore_finish(x, snapshot_id))
        self.status_label.setText("Collecting paths")
        self.setEnabled(False)
        self.thread.start()

    def reset_tree(self):
        self.index = {}
        self.expanded = set()
        self.hidden = {}
        self.dirs = {}
        self.snapshot = None

    def item_clicked(self, item):
        if self.index[item] in self.expanded:
            return
        if self.index[item] in self.dirs:
            item.removeChild(self.hidden[item])
            self.expanded.add(self.index[item])
            self.add_dir(self.index[item], item)

    def list_dir(self, path):
        return self.dirs[path]

    def add_dir(self, dir_path, parent):
        sorted_list = sorted(self.list_dir(dir_path),
                             key=lambda x: x not in self.dirs)
        for path in sorted_list:
            basename = os.path.basename(path)
            if len(basename) == 0:
                continue
            item = QTreeWidgetItem()
            item.setText(0, basename)
            self.index[item] = path
            parent.setFlags(parent.flags() | Qt.ItemIsTristate
                            | Qt.ItemIsUserCheckable)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(
                0, Qt.Checked
                if parent.checkState(0) == Qt.Checked else Qt.Unchecked)
            parent.addChild(item)
            if path in self.dirs and len(self.list_dir(path)) != 0:
                sub_item = QTreeWidgetItem()
                self.hidden[item] = sub_item
                item.addChild(sub_item)
                item.setIcon(0, QIcon(get_resource_path("images/folder.png")))

    def get_root_paths(self):
        min_path_depth = min(len(path) for path in self.dirs)
        roots = []
        for path in self.dirs:
            if len(path) is min_path_depth:
                roots.append(path)
        return roots

    def add_root_path(self, path):
        root = QTreeWidgetItem()
        root.setText(0, path)
        root.setCheckState(0, Qt.Unchecked)
        root.setIcon(0, QIcon(get_resource_path("images/folder.png")))
        self.index[root] = path
        self.expanded.add(path)
        self.snapshot_tree_widget.addTopLevelItem(root)
        self.add_dir(path, root)

    def populated_dirs(self, dirs):
        self.dirs = dirs
        for root in self.get_root_paths():
            self.add_root_path(root)
        self.status_label.clear()
        self.setEnabled(True)

    def populate_tree(self, snapshot):
        self.reset_tree()
        self.snapshot = snapshot

        self.dirs_thread = PopulateDirsThread(snapshot)
        self.dirs_thread.result.connect(self.populated_dirs)
        self.dirs_thread.start()

    def populate_snapshot(self):
        self.snapshot_tree_widget.clear()
        if self.snapshots_combo_box.count() is 0:
            return
        snapshot_id = self.snapshot_ids_to_str[
            self.snapshots_combo_box.currentText()]
        self.thread = DownloadSnapshotThread(self.backup, snapshot_id)
        self.thread.downloaded.connect(self.populate_tree)
        self.thread.start()

        self.status_label.setText("Loading snapshot")
        self.setEnabled(False)

    def populate_snapshots(self):
        self.snapshots_combo_box.clear()
        snapshot_ids = sorted(Repo(Utils.get_backend(
            self.backup)).get_snapshot_ids(),
                              reverse=True)
        for snapshot_id in snapshot_ids:
            time_str = f"{pretty_time(snapshot_id)} ({snapshot_id})"
            self.snapshot_ids_to_str[time_str] = snapshot_id
            self.snapshots_combo_box.addItem(time_str)
        self.populate_snapshot()
        if self.snapshots_combo_box.count() is 0:
            QMessageBox.warning(
                self.window, "No Snapshots",
                "There are no snapshots available for viewing in this backup.")
