import requests

from framework.models import ListData, BoardData
from framework.api.base_api import BaseAPI
from framework.constants import DEFAULT_HOST
from dataclasses import asdict


class ListAPI(BaseAPI):
    def __init__(self, token, key, host=DEFAULT_HOST):
        super().__init__(token, key, host)
        self.base_url = f'{self.host}/1/lists/'

    def get_list(self, list_id, fields=None):
        url = f'{self.base_url}{list_id}'

        if fields:
            fields_param = {"fields": fields}
            params = {**self.auth_params, **fields_param}
        else:
            params = self.auth_params
        response = self.session.get(url, params=params)
        list_data = ListData(**response.json()) if response.ok else None
        return response.status_code, list_data

    def get_list_board(self, list_id):
        url = f'{self.base_url}{list_id}/board'

        params = self.auth_params
        response = self.session.get(url, params=params)
        board_data = BoardData(**response.json()) if response.ok else None
        return response.status_code, board_data

    def create_list(self, name, id_board=None):
        url = self.base_url
        if id_board:
            data = {
                "name": name,
                "idBoard": id_board
            }
        else:
            data = {
                "name": name
            }
        response = self.session.post(url, json=data, params=self.auth_params)
        list_data = ListData(**response.json()) if response.ok else None
        return response.status_code, list_data

    def update_list(self, list_id, new_list_data):
        url = f'{self.base_url}{list_id}'
        data = asdict(new_list_data)
        response = self.session.put(url, json=data, params=self.auth_params)
        list_data = ListData(**response.json()) if response.ok else None
        return response.status_code, list_data
