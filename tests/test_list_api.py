import pytest
import requests
from hamcrest import assert_that, equal_to, none
from requests import codes
from framework.api.board_api import BoardAPI
from framework.matcher import check_list_data, check_status_code, check_id_name
from framework.constants import INVALID_ID
from framework.models import ListData


@pytest.mark.list
class TestListApi:
    @pytest.mark.positive
    def test_get_list(self, list_api, list_):
        status_code, list_response = list_api.get_list(list_.id)

        check_status_code(status_code, codes.ok)
        check_list_data(list_response, list_)

    @pytest.mark.positive
    def test_get_list_only_name(self, list_api, list_):
        status_code, list_response = list_api.get_list(list_.id, "name")

        check_status_code(status_code, codes.ok)
        check_id_name(list_response, list_)
        assert_that(list_response.idBoard, none())

    @pytest.mark.positive
    def test_get_list_board(self, list_api, list_):
        status_code, board_response = list_api.get_list_board(list_.id)

        check_status_code(status_code, codes.ok)
        assert_that(board_response.id, equal_to(list_.idBoard))

    @pytest.mark.positive
    def test_create_list(self, list_api, board, random_name):
        status_code, list_response = list_api.create_list(random_name, board.id)

        check_status_code(status_code, codes.ok)
        expected_list = ListData(id=list_response.id, name=random_name, idBoard=board.id)
        check_id_name(list_response, expected_list)

        status_code, get_response = list_api.get_list(expected_list.id)
        check_status_code(status_code, codes.ok)
        check_list_data(get_response, expected_list)

    @pytest.mark.negative
    def test_create_list_invalid_board(self, list_api, random_name):
        status_code, list_response = list_api.create_list(random_name, INVALID_ID)

        check_status_code(status_code, codes.bad_request)

    @pytest.mark.negative
    def test_create_list_without_board(self, list_api, random_name):
        status_code, list_response = list_api.create_list(random_name)

        check_status_code(status_code, codes.bad_request)

    @pytest.mark.positive
    def test_update_list_name(self, list_api, list_, random_name):
        new_list_data = ListData(id=list_.id, name=random_name, idBoard=list_.idBoard)
        status_code, list_response = list_api.update_list(list_.id, new_list_data)

        check_status_code(status_code, codes.ok)

        check_list_data(list_response, new_list_data)

    @pytest.mark.positive
    def test_update_list_board(self, list_api, list_, board):
        new_list_data = ListData(id=list_.id, name=list_.name, idBoard=board.id)
        status_code, list_response = list_api.update_list(list_.id, new_list_data)

        check_status_code(status_code, codes.ok)

        check_list_data(list_response, new_list_data)
