from PySide2.QtWidgets import QDialog, QDialogButtonBox, QMessageBox, QFileDialog
from ui_config_local_dialog import Ui_ConfigLocalDialog
from validator import Validator
from models import Backup, Backups
from command_thread import CommandThread, config_worker


class ConfigLocalDialog(QDialog, Ui_ConfigLocalDialog):
    def __init__(self, window, just_save=False):
        QDialog.__init__(self)
        Ui_ConfigLocalDialog.__init__(self)

        self.setupUi(self)
        self.window = window
        self.backup = None

        self.just_save = just_save

        if self.just_save:
            self.confirm_password_line_edit.hide()
            self.label_3.hide()

        self.browse_button.pressed.connect(self.browse)

    def browse(self):
        directory = QFileDialog.getExistingDirectory()
        self.local_directory_line_edit.setText(directory)

    def command_done(self, res):
        self.setEnabled(True)

        ret, message = res
        if not ret:
            QMessageBox.warning(self.window, "Invalid details", message)
            return

        if self.just_save:
            Backups.save(self.backup)

        super().accept()

    def accept(self):
        name = self.name_line_edit.text().strip()
        password = self.password_line_edit.text()
        if self.just_save:
            confirm_password = password
        else:
            confirm_password = self.confirm_password_line_edit.text()
        directory = self.local_directory_line_edit.text()

        backup = Backup()
        backup.name = name
        backup.location = "Local Directory"
        backup.password = password
        backup.local_directory = directory
        self.backup = backup

        fs = [
            Validator.validate_plan_name, Validator.validate_confirm_password,
            Validator.validate_local_path, Validator.validate_backend,
            Validator.validate_repo
        ]
        args = [(name, ), (password, confirm_password), (directory, ),
                (backup, ), (backup, self.just_save)]
        self.setEnabled(False)
        self.thread = CommandThread(config_worker, {"fs": fs, "args": args})
        self.thread.result.connect(self.command_done)
        self.thread.start()