import requests

from blobbackup.util import hash_password
from blobbackup.config import config
from blobbackup.logger import get_logger

BASE_API_URL = config["meta"]["server"] + "/api"


def login(email, password):
    url = BASE_API_URL + "/login"
    logger, hashed_password = get_logger_and_password(email, password)
    try:
        response = requests.get(url, auth=(email, hashed_password))
        if response.status_code != 200:
            logger.error("Login failed")
            return None
        user = response.json()
        return user
    except requests.exceptions.ConnectionError:
        logger.error("Login connection error.")
        return None


def create_new_computer(email, password, name, operating_system):
    url = BASE_API_URL + "/computers"
    logger, hashed_password = get_logger_and_password(email, password)
    try:
        response = requests.post(
            url,
            auth=(email, hashed_password),
            data={"name": name, "operating_system": operating_system},
        )
        if response.status_code != 201:
            logger.error("Computer creation failed.")
            return None
        computer = response.json()
        return computer
    except requests.exceptions.ConnectionError:
        logger.error("Computer creation connection error.")
        return None


def update_computer(email, password, computer_id, fields):
    url = BASE_API_URL + "/computers/" + str(computer_id)
    logger, hashed_password = get_logger_and_password(email, password)
    try:
        response = requests.post(
            url,
            auth=(email, hashed_password),
            data=fields,
        )
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        logger.error("Computer update connection error.")
        return False


def get_computer(email, password, computer_id):
    url = BASE_API_URL + "/computers/" + str(computer_id)
    logger, hashed_password = get_logger_and_password(email, password)
    response = requests.get(url, auth=(email, hashed_password))
    if response.status_code != 200:
        logger.error("Computer fetch failed.")
        return None
    computer = response.json()
    return computer


def get_computers(email, password):
    url = BASE_API_URL + "/computers"
    logger, hashed_password = get_logger_and_password(email, password)
    try:
        response = requests.get(url, auth=(email, hashed_password))
        if response.status_code != 200:
            logger.error("Computers fetch failed.")
            return None
        computers = response.json()
        return computers
    except requests.exceptions.ConnectionError:
        logger.error("Computers fetch connection error.")
        return None


def get_logger_and_password(email, password):
    hashed_password = hash_password(password, email)
    logger = get_logger()
    return logger, hashed_password
