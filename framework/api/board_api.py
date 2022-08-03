from framework.api.base_api import BaseAPI
from framework.models import BoardData
from framework.constants import DEFAULT_HOST


class BoardAPI(BaseAPI):
    def __init__(self, token, key, host=DEFAULT_HOST):
        super().__init__(token, key, host)
        self.base_url = f'{self.host}/1/boards/'

    def get_board(self, board_id):
        url = f'{self.base_url}{board_id}'
        response = self.session.get(url, params=self.auth_params)
        board_data = BoardData(**response.json()) if response.ok else None
        return response.status_code, board_data

    def create_board(self, name=None, default_labels=True):
        url = self.base_url
        data = {
            "defaultLabels": default_labels
        }
        name_param = {'name': name}
        response = self.session.post(url, json=data, params={**self.auth_params, **name_param})
        board_data = BoardData(**response.json()) if response.ok else None
        return response.status_code, board_data

    def delete_board(self, board_id):
        url = f'{self.base_url}{board_id}'
        response = self.session.delete(url, params=self.auth_params)
        return response.status_code
