import pytest
import requests
from hamcrest import assert_that, equal_to
from requests import codes
from framework.api.board_api import BoardAPI
from framework.matcher import check_board_data, check_status_code, check_board_name
from framework.constants import INVALID_ID


@pytest.mark.positive
@pytest.mark.board
def test_get_board(board_api, board):
    status_code, board_response = board_api.get_board(board.id)

    check_status_code(status_code, codes.ok)
    check_board_data(board_response, board)


@pytest.mark.negative
@pytest.mark.board
def test_get_board_invalid_id(board_api):
    status_code, board_response = board_api.get_board(INVALID_ID)

    check_status_code(status_code, codes.bad_request)


@pytest.mark.positive
@pytest.mark.board
@pytest.mark.parametrize('default_labels', [True, False])
def test_create_board(board_api, random_name, default_labels):
    status_code, board_response = board_api.create_board(random_name, default_labels)

    check_status_code(status_code, codes.ok)
    check_board_name(board_response, random_name)

    board_api.delete_board(board_response.id)


@pytest.mark.negative
@pytest.mark.board
def test_create_board_without_name(board_api):
    status_code, board_response = board_api.create_board()

    check_status_code(status_code, codes.bad_request)
