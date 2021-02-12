from PySide2.QtWidgets import QDialog, QDialogButtonBox, QMessageBox, QFileDialog
from ui_config_sftp_dialog import Ui_ConfigSFTPDialog
from validator import Validator
from models import Backup, Backups
from command_thread import CommandThread, config_worker


class ConfigSFTPDialog(QDialog, Ui_ConfigSFTPDialog):
    def __init__(self, window, just_save):
        QDialog.__init__(self)
        Ui_ConfigSFTPDialog.__init__(self)

        self.setupUi(self)
        self.window = window
        self.backup = None
        self.just_save = just_save

        if self.just_save:
            self.confirm_password_line_edit.hide()
            self.label_3.hide()

        self.browse_button.pressed.connect(self.browse)

    def browse(self):
        path, _ = QFileDialog.getOpenFileName()
        self.private_key_line_edit.setText(path)

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
        private_key = self.private_key_line_edit.text()
        username = self.username_line_edit.text().strip()
        sftp_password = self.sftp_password_line_edit.text().strip()
        server = self.server_line_edit.text().strip()
        prefix = self.prefix_line_edit.text().strip()

        backup = Backup()
        backup.name = name
        backup.location = "SFTP"
        backup.password = password
        if len(private_key) is not 0:
            backup.sftp_private_key = private_key
        backup.sftp_username = username
        if len(sftp_password) is not 0:
            backup.sftp_password = sftp_password
        backup.sftp_server = server
        backup.cloud_prefix = prefix
        self.backup = backup

        fs = [
            Validator.validate_plan_name, Validator.validate_confirm_password,
            Validator.validate_non_empty, Validator.validate_non_empty,
            Validator.validate_non_empty, Validator.validate_no_space,
            Validator.validate_no_space, Validator.validate_no_space,
            Validator.validate_backend, Validator.validate_repo
        ]
        args = [(name, ), (password, confirm_password), ("Username", username),
                ("Server", server), ("Prefix", prefix), ("Server", server),
                ("Prefix", prefix), ("Username", username), (backup, ),
                (backup, self.just_save)]
        self.setEnabled(False)
        self.thread = CommandThread(config_worker, {"fs": fs, "args": args})
        self.thread.result.connect(self.command_done)
        self.thread.start()