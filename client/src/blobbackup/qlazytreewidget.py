import os

from collections import defaultdict

from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

from blobbackup.util import FOLDER_PATH


def prepare_lazy_tree(nodes):
    tree = defaultdict(list)
    nodes_set = set(["/"])
    for node in nodes:
        nodes_set.add(node)
        next_node = os.path.dirname(node)
        if next_node not in nodes_set:
            while next_node != "/":
                nodes_set.add(next_node)
                next_node = os.path.dirname(next_node)
    for node in nodes_set:
        dirname = os.path.dirname(node)
        if node != dirname:
            tree[dirname].append(node)
    return tree


def get_selected_nodes(tree_widget):
    selected_nodes = []
    for item in tree_widget.findItems("", Qt.MatchFlag.MatchContains | Qt.MatchFlag.MatchRecursive):
        if item.checkState(0) == Qt.CheckState.Checked:
            node = item.whatsThis(0)
            selected_nodes.append(node)
    return selected_nodes


class QLazyTreeWidget(QTreeWidget):
    def __init__(self):
        QTreeWidget.__init__(self)
        self.itemExpanded.connect(self._item_expanded)
        self.setHeaderHidden(True)

    def initialize(self, tree, computer_name):
        self.loaded_nodes = set()
        self.placeholders = {}
        self.tree = tree
        self.clear()
        self._populate_initial(computer_name)

    def _populate_initial(self, computer_name):
        item = QTreeWidgetItem([computer_name])
        item.setWhatsThis(0, "/")
        item.setIcon(0, QIcon(FOLDER_PATH))
        self.addTopLevelItem(item)
        self._populate_children(item, "/")

    def _populate_children(self, parent_item, parent_node):
        self.loaded_nodes.add(parent_node)
        parent_item.setFlags(
            parent_item.flags() | Qt.ItemFlag.ItemIsAutoTristate | Qt.ItemFlag.ItemIsUserCheckable
        )
        for node in sorted(self.tree[parent_node], key=lambda n: n not in self.tree):
            item = QTreeWidgetItem([os.path.basename(node)])
            item.setWhatsThis(0, node)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(
                0,
                Qt.CheckState.Checked if parent_item.checkState(0) == Qt.CheckState.Checked else Qt.CheckState.Unchecked,
            )
            parent_item.addChild(item)
            if node in self.tree:
                placeholder_item = QTreeWidgetItem([".."])
                self.placeholders[node] = placeholder_item
                item.addChild(placeholder_item)
                item.setIcon(0, QIcon(FOLDER_PATH))

    def _item_expanded(self, item):
        node = item.whatsThis(0)
        if node not in self.loaded_nodes:
            item.removeChild(self.placeholders[node])
            self._populate_children(item, node)
