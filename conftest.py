import pytest

from faker import Faker
from framework.api.board_api import BoardAPI
from config import TOKEN, KEY


faker = Faker()


@pytest.fixture(scope='session')
def board_api():
    return BoardAPI(TOKEN, KEY)


@pytest.fixture(scope='function')
def random_name():
    return faker.word()


@pytest.fixture(scope='function')
def board(board_api, random_name):
    _, board = board_api.create_board(name=random_name)

    yield board

    board_api.delete_board(board.id)



