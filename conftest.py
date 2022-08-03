import pytest

from faker import Faker
from framework.api.board_api import BoardAPI
from framework.api.list_api import ListAPI
from framework.api.card_api import CardAPI
from config import TOKEN, KEY


faker = Faker()


@pytest.fixture(scope='session')
def board_api():
    return BoardAPI(TOKEN, KEY)


@pytest.fixture(scope='session')
def list_api():
    return ListAPI(TOKEN, KEY)


@pytest.fixture(scope='session')
def card_api():
    return CardAPI(TOKEN, KEY)


@pytest.fixture(scope='function')
def random_name():
    return faker.word()


@pytest.fixture(scope='function')
def random_company():
    return faker.company()


@pytest.fixture(scope='function')
def random_text():
    return faker.sentence()


@pytest.fixture(scope='function')
def board(board_api, random_name):
    _, board = board_api.create_board(name=random_name)

    yield board

    board_api.delete_board(board.id)


@pytest.fixture(scope='function')
def list_(board, list_api, random_name):
    _, list_ = list_api.create_list(name=random_name, id_board=board.id)

    return list_


@pytest.fixture(scope='function')
def card(list_, card_api, random_name):
    _, card = card_api.create_card(name=random_name, id_list=list_.id)

    return card



