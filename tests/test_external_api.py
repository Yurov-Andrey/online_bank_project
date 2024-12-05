from unittest.mock import patch

import pytest

from src.external_api import currency_conversion


def test_currency_conversion_rub(test_fixture_dict_conversion_rub):
    assert currency_conversion(test_fixture_dict_conversion_rub) == 8221.37


@patch('requests.request')
def test_currency_conversion_usd(mock_get, test_fixture_dict_conversion_usd):
    mock_get.return_value.json.return_value = {
        "date": "2024-12-05",
        "info": {
            "rate": 105.00057,
            "timestamp": 1733380935
        },
        "query": {
            "amount": 8221.37,
            "from": "USD",
            "to": "RUB"
        },
        "result": 863248.536181,
        "success": True
    }
    assert currency_conversion(test_fixture_dict_conversion_usd) == 863248.54
    mock_get.currency_conversion(
        "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={currency}&amount={amount}")


def test_currency_conversion_invalid_type(test_fixture_dict_conversion_invalid_type):
    with pytest.raises(ValueError) as exc_info:
        currency_conversion(test_fixture_dict_conversion_invalid_type)

    assert str(exc_info.value) == "Не верный тип данных входящей транзакции"


def test_dict_conversion_invalid_oa(test_fixture_dict_conversion_invalid_oa):
    with pytest.raises(ValueError) as exc_info:
        currency_conversion(test_fixture_dict_conversion_invalid_oa)

    assert str(exc_info.value) == "Не найдено значение 'operationAmount'"


def test_dict_conversion_invalid_amount(test_fixture_dict_conversion_invalid_amount):
    with pytest.raises(ValueError) as exc_info:
        currency_conversion(test_fixture_dict_conversion_invalid_amount)

    assert str(exc_info.value) == "Не найдено значение 'amount'"


def test_dict_conversion_invalid_currency(test_fixture_dict_conversion_invalid_currency):
    with pytest.raises(ValueError) as exc_info:
        currency_conversion(test_fixture_dict_conversion_invalid_currency)

    assert str(exc_info.value) == "Не найдено значение 'currency'"


def test_dict_conversion_invalid_sum(test_fixture_dict_conversion_invalid_sum):
    with pytest.raises(ValueError) as exc_info:
        currency_conversion(test_fixture_dict_conversion_invalid_sum)

    assert str(exc_info.value) == "Сумма транзакции равна нулю или отсутствует"


def test_dict_conversion_invalid_code(test_fixture_dict_conversion_invalid_code):
    with pytest.raises(ValueError) as exc_info:
        currency_conversion(test_fixture_dict_conversion_invalid_code)

    assert str(exc_info.value) == "Не найдено значение 'code'"


def test_dict_conversion_invalid_code_data(test_fixture_dict_conversion_invalid_code_data):
    with pytest.raises(ValueError) as exc_info:
        currency_conversion(test_fixture_dict_conversion_invalid_code_data)

    assert str(exc_info.value) == "Валюта транзакции не найдена"
