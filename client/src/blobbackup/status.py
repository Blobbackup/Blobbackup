import os


from blobbackup.util import HOME_PATH


LAST_BACKED_UP_PATH = os.path.join(HOME_PATH, "lastbackedup.txt")
SELECTED_FILES_PATH = os.path.join(HOME_PATH, "selectedfiles.txt")
CURRENT_STATUS_PATH = os.path.join(HOME_PATH, "currentstatus.txt")


def save_generic(path, data):
    with open(path, "w", encoding="utf-8") as f:
        f.write(data)


def get_generic(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def save_last_backed_up(last_backed_up):
    return save_generic(LAST_BACKED_UP_PATH, last_backed_up)


def get_last_backed_up():
    return get_generic(LAST_BACKED_UP_PATH)


def save_selected_files(selected_files):
    return save_generic(SELECTED_FILES_PATH, selected_files)


def get_selected_files():
    return get_generic(SELECTED_FILES_PATH)


def save_current_status(current_status):
    return save_generic(CURRENT_STATUS_PATH, current_status)


def get_current_status():
    return get_generic(CURRENT_STATUS_PATH)
