from hamcrest import assert_that, equal_to


def check_id_name(actual_data, expected_data):
    assert_that(
        actual_data.id, equal_to(expected_data.id),
        f'Id is {actual_data.id}'
    )
    assert_that(
        actual_data.name, equal_to(expected_data.name),
        f'Name is {actual_data.name}'
    )


def check_board_data(actual_data, expected_data):
    check_id_name(actual_data, expected_data)
    assert_that(
        actual_data.url, equal_to(expected_data.url),
        f'Url is {actual_data.url}'
    )


def check_list_data(actual_data, expected_data):
    check_id_name(actual_data, expected_data)
    assert_that(
        actual_data.idBoard, equal_to(expected_data.idBoard),
        f'idBoard is {actual_data.idBoard}'
    )


def check_card_data(actual_data, expected_data):
    check_id_name(actual_data, expected_data)
    assert_that(
        actual_data.idList, equal_to(expected_data.idList),
        f'idList is {actual_data.idList}'
    )


def check_name(actual_data, expected_name):
    assert_that(
        actual_data.name, equal_to(expected_name),
        f'Name is {actual_data.name}'
    )


def check_status_code(status_code, expected_status_code):
    assert_that(
        status_code, equal_to(expected_status_code),
        f'Status code is {status_code}'
    )
