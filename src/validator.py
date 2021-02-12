import os
from models import Backups, Utils
from repo2 import Repo


class Validator(object):
    @staticmethod
    def validate_plan_name(name):
        if len(name) is 0:
            return False, "Backup name must not be empty"
        if name in Backups.load_all():
            return False, "Backup name is already in use"
        return True, None

    @staticmethod
    def validate_password(password):
        if len(password) is 0:
            return False, "Password cannot be empty"
        if len(password) < 8:
            return False, "Password must be at least 8 characters long"
        return True, None

    @staticmethod
    def validate_confirm_password(password, confirm_password):
        ret, message = Validator.validate_password(password)
        if not ret:
            return ret, message
        if password != confirm_password:
            return False, "Passwords must match"
        return True, None

    @staticmethod
    def validate_local_path(path):
        if len(path) is 0:
            return False, "Path must not be empty"
        if not os.path.exists(path):
            return False, "Path does not exist"
        return True, None

    @staticmethod
    def validate_non_empty(name, item):
        if len(item) is 0:
            return False, f"{name} cannot be empty"
        return True, None

    @staticmethod
    def validate_no_space(name, item):
        if " " in item:
            return False, f"{name} cannot contain spaces"
        return True, None

    @staticmethod
    def validate_backend(backup):
        try:
            if not Utils.get_backend(backup).check_connection():
                return False, f"Cannot connect to {backup.location} backend"
        except:
            return False, f"Cannot connect to {backup.location} backend"
        return True, None

    @staticmethod
    def validate_repo(backup, just_save):
        backend = Utils.get_backend(backup)
        if not backend.check_connection():
            return False, "Connection error"
        if just_save:
            repo = Repo(backend)
            if not repo.is_initialized():
                return False, "This destination is not initialized"
            if not repo.check_password(backup.password.encode()):
                return False, "Password incorrect"
        else:
            repo = Repo(backend)
            if repo.is_initialized():
                return False, "This destination is already initialized"
        return True, None

    @staticmethod
    def validate(fs, args):
        for f, arg in zip(fs, args):
            ret, message = f(*arg)
            if not ret:
                return ret, message
        return True, None