import requests

from framework.models import ListData, BoardData, CardData
from framework.api.base_api import BaseAPI
from framework.constants import DEFAULT_HOST
from dataclasses import asdict


class CardAPI(BaseAPI):
    def __init__(self, token, key, host=DEFAULT_HOST):
        super().__init__(token, key, host)
        self.base_url = f'{self.host}/1/cards/'

    def get_card(self, card_id, auth=True):
        url = f'{self.base_url}{card_id}'
        if auth:
            params = self.auth_params
        else:
            params = {}
        response = self.session.get(url, params=params)
        card_data = CardData(**response.json()) if response.ok else None
        return response.status_code, card_data

    def create_card(self, name, id_list=None):
        url = self.base_url
        if id_list:
            data = {
                "name": name,
                "idList": id_list
            }
        else:
            data = {
                "name": name
            }
        response = self.session.post(url, json=data, params=self.auth_params)
        card_data = CardData(**response.json()) if response.ok else None
        return response.status_code, card_data

    def update_card(self, card_id, new_card_data):
        url = f'{self.base_url}{card_id}'
        data = asdict(new_card_data)
        response = self.session.put(url, json=data, params=self.auth_params)
        card_data = CardData(**response.json()) if response.ok else None
        return response.status_code, card_data

    def delete_card(self, card_id):
        url = f'{self.base_url}{card_id}'
        response = self.session.delete(url, params=self.auth_params)
        return response.status_code

    def add_comment(self, card_id, text):
        url = f'{self.base_url}{card_id}/actions/comments'
        data = {
            "text": text
        }
        response = self.session.post(url, json=data, params=self.auth_params)
        text_data = response.json().get('data').get('text') if response.ok else None
        return response.status_code, text_data
