import requests

from framework.models import BoardData


class BoardAPI:
    def __init__(self, token, key, host='https://api.trello.com'):
        self.host = host
        self.session = requests.Session()
        self.auth_params = {'token': token, 'key': key}

    def get_board(self, board_id):
        url = f'{self.host}/1/boards/{board_id}'
        response = self.session.get(url, params=self.auth_params)
        board_data = BoardData(**response.json()) if response.ok else None
        return response.status_code, board_data

    def create_board(self, name=None, default_labels=True):
        url = f'{self.host}/1/boards/'
        data = {
            "defaultLabels": default_labels
        }
        name_param = {'name': name}
        response = self.session.post(url, json=data, params={**self.auth_params, **name_param})
        board_data = BoardData(**response.json()) if response.ok else None
        return response.status_code, board_data

    def delete_board(self, board_id):
        url = f'{self.host}/1/boards/{board_id}'
        response = self.session.delete(url, params=self.auth_params)
        return response.status_code
