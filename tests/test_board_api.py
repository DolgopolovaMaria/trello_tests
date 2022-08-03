import pytest
from requests import codes
from framework.matcher import check_board_data, check_status_code, check_name
from framework.constants import INVALID_ID, NONEXISTENT_ID


@pytest.mark.board
class TestBoardApi:
    @pytest.mark.positive
    def test_get_board(self, board_api, board):
        status_code, board_response = board_api.get_board(board.id)

        check_status_code(status_code, codes.ok)
        check_board_data(board_response, board)

    @pytest.mark.negative
    def test_get_board_invalid_id(self, board_api):
        status_code, board_response = board_api.get_board(INVALID_ID)

        check_status_code(status_code, codes.bad_request)

    @pytest.mark.negative
    def test_get_board_nonexistent_id(self, board_api):
        status_code, board_response = board_api.get_board(NONEXISTENT_ID)

        check_status_code(status_code, codes.not_found)

    @pytest.mark.positive
    @pytest.mark.parametrize('default_labels', [True, False])
    def test_create_board(self, board_api, random_name, default_labels):
        status_code, board_response = board_api.create_board(random_name, default_labels)

        check_status_code(status_code, codes.ok)
        check_name(board_response, random_name)

        board_api.delete_board(board_response.id)

    @pytest.mark.negative
    def test_create_board_without_name(self, board_api):
        status_code, board_response = board_api.create_board()

        check_status_code(status_code, codes.bad_request)

    @pytest.mark.positive
    def test_delete_board(self, board_api, board):
        status_code = board_api.delete_board(board.id)

        check_status_code(status_code, codes.ok)
