import pytest
import requests
from hamcrest import assert_that, equal_to, none
from requests import codes
from framework.api.board_api import BoardAPI
from framework.matcher import check_list_data, check_status_code, check_id_name, check_card_data
from framework.constants import INVALID_ID, NONEXISTENT_ID
from framework.models import CardData


@pytest.mark.card
class TestCardApi:
    @pytest.mark.positive
    def test_get_card(self, card_api, card):
        status_code, card_response = card_api.get_card(card.id)

        check_status_code(status_code, codes.ok)
        check_card_data(card_response, card)

    @pytest.mark.negative
    def test_get_card_without_auth(self, card_api, card):
        status_code, card_response = card_api.get_card(card.id, False)

        check_status_code(status_code, codes.unauthorized)

    @pytest.mark.positive
    def test_create_card(self, card_api, list_, random_name):
        status_code, card_response = card_api.create_card(random_name, list_.id)

        check_status_code(status_code, codes.ok)
        expected_card = CardData(id=card_response.id, name=random_name, idList=list_.id)
        check_card_data(card_response, expected_card)

        status_code, get_response = card_api.get_card(expected_card.id)
        check_status_code(status_code, codes.ok)
        check_card_data(get_response, expected_card)

    @pytest.mark.negative
    def test_create_card_without_list(self, card_api, random_name):
        status_code, card_response = card_api.create_card(random_name)

        check_status_code(status_code, codes.bad_request)

    @pytest.mark.positive
    def test_update_card_name_list(self, card_api, card, list_, random_name):
        new_card_data = CardData(id=card.id, name=random_name, idList=list_.id)
        status_code, card_response = card_api.update_card(card.id, new_card_data)

        check_status_code(status_code, codes.ok)

        check_card_data(card_response, new_card_data)

    @pytest.mark.negative
    def test_update_card_invalid_list(self, card_api, card):
        new_card_data = CardData(id=card.id, name=card.name, idList=INVALID_ID)
        status_code, card_response = card_api.update_card(card.id, new_card_data)

        check_status_code(status_code, codes.bad_request)

    @pytest.mark.positive
    def test_delete_card(self, card_api, card):
        status_code = card_api.delete_card(card.id)

        check_status_code(status_code, codes.ok)

    @pytest.mark.negative
    def test_delete_nonexistent_card(self, card_api):
        status_code = card_api.delete_card(NONEXISTENT_ID)

        check_status_code(status_code, codes.not_found)

    @pytest.mark.positive
    def test_add_comment_card(self, card_api, card, random_text):
        status_code, response_text = card_api.add_comment(card.id, random_text)

        check_status_code(status_code, codes.ok)

        assert_that(response_text, equal_to(random_text),
                    f'Text is {response_text}')