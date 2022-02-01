import requests

from blobbackup.util import BASE_APP_URL, hash_password

BASE_API_URL = BASE_APP_URL + "/api"


def login(email, password):
    url = BASE_API_URL + "/login"
    hashed_password = hash_password(password, email)
    try:
        response = requests.get(url, auth=(email, hashed_password))
        if response.status_code != 200:
            return None
        user = response.json()
        return user
    except requests.exceptions.ConnectionError:
        return None


def create_new_computer(email, password, name, operating_system):
    url = BASE_API_URL + "/computers"
    hashed_password = hash_password(password, email)
    try:
        response = requests.post(
            url,
            auth=(email, hashed_password),
            data={"name": name, "operating_system": operating_system},
        )
        if response.status_code != 201:
            return None
        computer = response.json()
        return computer
    except requests.exceptions.ConnectionError:
        return None


def update_computer(email, password, computer_id, fields):
    url = BASE_API_URL + "/computers/" + str(computer_id)
    hashed_password = hash_password(password, email)
    try:
        response = requests.post(
            url,
            auth=(email, hashed_password),
            data=fields,
        )
        return response.status_code == 200
    except requests.exceptions.ConnectionError:
        return False


def get_computer(email, password, computer_id):
    url = BASE_API_URL + "/computers/" + str(computer_id)
    hashed_password = hash_password(password, email)
    try:
        response = requests.get(url, auth=(email, hashed_password))
        if response.status_code != 200:
            return None
        computer = response.json()
        return computer
    except requests.exceptions.ConnectionError:
        return None


def get_computers(email, password):
    url = BASE_API_URL + "/computers"
    hashed_password = hash_password(password, email)
    try:
        response = requests.get(url, auth=(email, hashed_password))
        if response.status_code != 200:
            return None
        computers = response.json()
        return computers
    except requests.exceptions.ConnectionError:
        return None
