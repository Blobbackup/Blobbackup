from PySide2.QtWidgets import QDialog, QDialogButtonBox, QMessageBox, QFileDialog
from ui_config_aws_dialog import Ui_ConfigAwsDialog
from validator import Validator
from models import Backup, Backups
from command_thread import CommandThread, config_worker


class ConfigAwsDialog(QDialog, Ui_ConfigAwsDialog):
    def __init__(self, window, just_save=False):
        QDialog.__init__(self)
        Ui_ConfigAwsDialog.__init__(self)

        self.setupUi(self)
        self.window = window
        self.backup = None
        self.just_save = just_save

        if self.just_save:
            self.confirm_password_line_edit.hide()
            self.label_3.hide()

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
        key_id = self.key_id_line_edit.text().strip()
        key = self.key_line_edit.text().strip()
        bucket = self.bucket_line_edit.text().strip()
        prefix = self.prefix_line_edit.text().strip()

        backup = Backup()
        backup.name = name
        backup.location = "Amazon AWS"
        backup.password = password
        backup.aws_key_id = key_id
        backup.aws_key = key
        backup.aws_bucket = bucket
        backup.cloud_prefix = prefix
        self.backup = backup

        fs = [Validator.validate_plan_name, Validator.validate_confirm_password,
            Validator.validate_non_empty, Validator.validate_non_empty,
            Validator.validate_non_empty, Validator.validate_non_empty,
            Validator.validate_no_space, Validator.validate_no_space,
            Validator.validate_backend, Validator.validate_repo]
        args = [(name, ), (password, confirm_password), ("AWS Key Id", key_id),
            ("AWS Key", key), ("Bucket", bucket), ("Prefix", prefix),
            ("Bucket", bucket), ("Prefix", prefix), (backup, ),
            (backup, self.just_save)]
        self.setEnabled(False)
        self.thread = CommandThread(config_worker, {"fs": fs, "args": args})
        self.thread.result.connect(self.command_done)
        self.thread.start()
