import pytest
from src.func import json_encode, last_five_operations, get_data_format, format_date, format_card


@pytest.fixture
def operations():
    return [{
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }]


@pytest.fixture
def operation_one():
    return [{
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    }]


def test_last_five_operation(operations):
    assert [operation["id"] for operation in operations] == [142264268, 873106923]
    assert [operation["state"] for operation in operations] == ["EXECUTED", "EXECUTED"]


def test_format_card():
    assert format_card("Visa Gold 5999414228426353") == "Visa Gold 5999 41** **** 6353"


def test_format_date():
    assert format_date("2019-03-23T01:09:46.296404") == "23.03.2019"
    assert format_date("2018-04-04T17:33:34.701093") == "04.04.2018"


def test_get_data_format(operation_one):
    assert type(get_data_format(operation_one)) != list
    assert [operation["description"] for operation in operation_one] == ["Перевод со счета на счет"]
