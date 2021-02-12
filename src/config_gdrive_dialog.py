from PySide2.QtWidgets import QDialog, QDialogButtonBox, QMessageBox, QFileDialog
from ui_config_gdrive_dialog import Ui_ConfigGDriveDialog
from validator import Validator
from models import Backup, Backups, BLOBBACKUP_DIR
from command_thread import CommandThread, config_worker

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import pickle

client_config = {
    "installed": {
        "client_id":
        "240610495346-bgpqlps4fvu1todj9ejtcvvrqf8ni72j.apps.googleusercontent.com",
        "project_id": "blobbackup-1602893615302",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url":
        "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": "bsfb7UknwHzenhkJkDTYqmdB",
        "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob", "http://localhost"]
    }
}


class ConfigGDriveDialog(QDialog, Ui_ConfigGDriveDialog):
    def __init__(self, window, just_save):
        QDialog.__init__(self)
        Ui_ConfigGDriveDialog.__init__(self)

        self.setupUi(self)
        self.window = window
        self.backup = None
        self.just_save = just_save

        if self.just_save:
            self.confirm_password_line_edit.hide()
            self.label_3.hide()

        self.sign_in_button.pressed.connect(self.authorize)

    def authorize(self):
        flow = InstalledAppFlow.from_client_config(
            client_config, ["https://www.googleapis.com/auth/drive"])
        creds = flow.run_local_server(port=0)
        if not creds:
            return
        self.creds = creds
        self.sign_in_button.setEnabled(False)

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
        creds_path = f"{BLOBBACKUP_DIR}/{name}_gdrive_creds"
        with open(creds_path, "wb") as f:
            pickle.dump(self.creds, f)
        folder_name = self.folder_name_line_edit.text().strip()

        backup = Backup()
        backup.name = name
        backup.location = "Google Drive"
        backup.password = password
        backup.gdrive_creds_path = creds_path
        backup.gdrive_folder_name = folder_name
        self.backup = backup

        fs = [
            Validator.validate_plan_name, Validator.validate_confirm_password,
            Validator.validate_local_path, Validator.validate_non_empty,
            Validator.validate_repo
        ]
        args = [(name, ), (password, confirm_password), (creds_path, ),
                ("Folder Name", folder_name), (backup, self.just_save)]
        self.setEnabled(False)
        self.thread = CommandThread(config_worker, {"fs": fs, "args": args})
        self.thread.result.connect(self.command_done)
        self.thread.start()
