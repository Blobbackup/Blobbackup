from PySide2.QtWidgets import QDialog, QDialogButtonBox, QMessageBox, QFileDialog
from ui_config_gcp_dialog import Ui_ConfigGcpDialog
from validator import Validator
from models import Backup, Backups
from command_thread import CommandThread, config_worker


class ConfigGcpDialog(QDialog, Ui_ConfigGcpDialog):
    def __init__(self, window, just_save):
        QDialog.__init__(self)
        Ui_ConfigGcpDialog.__init__(self)

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
        self.cred_file_line_edit.setText(path)

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
        cred_file = self.cred_file_line_edit.text()
        project = self.project_line_edit.text().strip()
        bucket = self.bucket_line_edit.text().strip()
        prefix = self.prefix_line_edit.text().strip()

        backup = Backup()
        backup.name = name
        backup.location = "Google Cloud"
        backup.password = password
        backup.gcp_cred_file = cred_file
        backup.gcp_project = project
        backup.gcp_bucket = bucket
        backup.cloud_prefix = prefix
        self.backup = backup

        fs = [Validator.validate_plan_name, Validator.validate_confirm_password,
            Validator.validate_local_path, Validator.validate_non_empty,
            Validator.validate_non_empty, Validator.validate_non_empty,
            Validator.validate_no_space, Validator.validate_no_space,
            Validator.validate_backend, Validator.validate_repo]
        args = [(name, ), (password, confirm_password), (cred_file, ),
            ("Project", project), ("Bucket", bucket), ("Prefix", prefix),
            ("Bucket", bucket), ("Prefix", prefix), (backup, ),
            (backup, self.just_save)]
        self.setEnabled(False)
        self.thread = CommandThread(config_worker, {"fs": fs, "args": args})
        self.thread.result.connect(self.command_done)
        self.thread.start()