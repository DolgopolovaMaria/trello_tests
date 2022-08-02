import requests
from framework.constants import DEFAULT_HOST


class BaseAPI:
    def __init__(self, token, key, host=DEFAULT_HOST):
        self.host = host
        self.session = requests.Session()
        self.auth_params = {'token': token, 'key': key}