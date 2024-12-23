import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from tests.conftest import test_fixture_transactions_for_generators_all_correct_dict


def test_filter_by_currency(test_fixture_transactions_for_generators_all_dict,
                            test_fixture_transactions_for_generators_all_correct_dict):
    usd_transactions = list(filter_by_currency(test_fixture_transactions_for_generators_all_dict, "USD"))
    assert usd_transactions == test_fixture_transactions_for_generators_all_correct_dict


def test_transactions_for_generators_invalid_currency(test_fixture_transactions_for_generators_invalid_currency):
    with pytest.raises(ValueError) as exc_info:
        list(filter_by_currency(test_fixture_transactions_for_generators_invalid_currency, "USD"))
        assert str(exc_info.value) == "Не найдено значение 'currency'"


def test_transactions_for_generators_invalid_operation_amount_key(
        test_fixture_transactions_for_generators_invalid_operation_amount_key):
    with pytest.raises(ValueError) as exc_info:
        list(filter_by_currency(test_fixture_transactions_for_generators_invalid_operation_amount_key, "USD"))
        assert str(exc_info.value) == "Не найдено значение 'operationAmount'"


def test_transactions_for_generators_invalid_name(test_fixture_transactions_for_generators_invalid_code):
    with pytest.raises(ValueError) as exc_info:
        list(filter_by_currency(test_fixture_transactions_for_generators_invalid_code, "USD"))
        assert str(exc_info.value) == "Не найдено значение 'code'"


def test_transaction_descriptions(test_fixture_transactions_for_generators_all_dict,
                                  test_fixture_transactions_for_generators_correct_description):
    transaction_description = list(transaction_descriptions(test_fixture_transactions_for_generators_all_dict))
    assert transaction_description == test_fixture_transactions_for_generators_correct_description


def test_transaction_descriptions_invalid_type(test_fixture_transactions_for_generators_correct_dict_1):
    with pytest.raises(ValueError) as exc_info:
        list(transaction_descriptions(test_fixture_transactions_for_generators_correct_dict_1))
        assert str(exc_info.value) == "Не верный тип данных входящих аргументов"


def test_transactions_for_generators_incorrect_list(test_fixture_transactions_for_generators_incorrect_list):
    with pytest.raises(ValueError) as exc_info:
        list(transaction_descriptions(test_fixture_transactions_for_generators_incorrect_list))
        assert str(exc_info.value) == "Не найдено значение 'description' или список транзакций отсутствует"


def test_transactions_for_generators_invalid_data_description(
        test_fixture_transactions_for_generators_invalid_data_description):
    with pytest.raises(ValueError) as exc_info:
        list(transaction_descriptions(test_fixture_transactions_for_generators_invalid_data_description))
        assert str(exc_info.value) == "Не верный тип данных или список транзакций отсутствует"


def test_transactions_for_generators_incorrect_list_2(test_fixture_transactions_for_generators_incorrect_list_2):
    with pytest.raises(ValueError) as exc_info:
        list(transaction_descriptions(test_fixture_transactions_for_generators_incorrect_list_2))
        assert str(exc_info.value) == "Не верный тип данных или список транзакций отсутствует"


def test_card_number_generator_correct_data(test_fixture_card_number_generator_correct_data):
    assert list(
        card_number_generator(1, 5)) == test_fixture_card_number_generator_correct_data


def test_number_generator_invalid_start_stop():
    with pytest.raises(ValueError) as exc_info:
        list(card_number_generator(2, 1))
        assert str(exc_info.value) == "Не верно заданы параметры start и stop, start должен быть меньше или равен stop"


def test_number_generator_invalid_type_arg():
    with pytest.raises(ValueError) as exc_info:
        list(card_number_generator("1", 5))
        assert str(exc_info.value) == "Не верный тип данных входящих аргументов"


def test_number_generator_invalid_len_arg():
    with pytest.raises(ValueError) as exc_info:
        list(card_number_generator(1, 99999999999999999))
        assert str(
            exc_info.value) == "Слишком большое число передано в start/end, максимальная длина строки не должна превышать 16 символов"


@pytest.mark.parametrize("start, stop", [(1, 5), (1, 5), (1, 5), (1, 5),
                                         (1, 5), ])
def test_number_generator_correct_param(start, stop):
    generator = card_number_generator(start, stop)
    assert next(generator) == '0000 0000 0000 0001'
    assert next(generator) == '0000 0000 0000 0002'
    assert next(generator) == '0000 0000 0000 0003'
    assert next(generator) == '0000 0000 0000 0004'
    assert next(generator) == '0000 0000 0000 0005'
