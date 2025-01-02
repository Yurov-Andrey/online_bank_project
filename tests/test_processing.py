import pytest

from src.processing import filter_by_state, sort_by_date, sort_by_search_string, sort_by_category
from tests.conftest import test_fixture_sort_by_date, test_fixture_sort_by_date_correct


def test_filter_by_state(test_fixture_filter_by_state_correct, test_fixture_filter_by_state_correct_executed):
    assert filter_by_state(test_fixture_filter_by_state_correct,
                           'EXECUTED') == test_fixture_filter_by_state_correct_executed


def test_filter_by_state_alt(test_fixture_filter_by_state_correct, test_fixture_filter_by_state_correct_canceled):
    assert filter_by_state(test_fixture_filter_by_state_correct,
                           'CANCELED') == test_fixture_filter_by_state_correct_canceled


def test_sort_by_date(test_fixture_sort_by_date, test_fixture_sort_by_date_correct):
    assert sort_by_date(test_fixture_sort_by_date) == test_fixture_sort_by_date_correct


def test_sort_by_search_string_card_to_card(
        test_fixture_dict_on_list_for_sort_func, test_fixture_dict_on_list_for_sort_func_correct_result_card_to_card
    ):
    search_string = 'Перевод с карты на карту'
    assert (sort_by_search_string
            (test_fixture_dict_on_list_for_sort_func, search_string)
            ) == test_fixture_dict_on_list_for_sort_func_correct_result_card_to_card

def test_sort_by_search_string_money_transfer(
        test_fixture_dict_on_list_for_sort_func, test_fixture_dict_on_list_for_sort_func_correct_result_money_transfer
    ):
    search_string = 'Перевод организации'
    assert (sort_by_search_string
            (test_fixture_dict_on_list_for_sort_func, search_string)
            ) == test_fixture_dict_on_list_for_sort_func_correct_result_money_transfer

def test_sort_by_search_string_deposit(
        test_fixture_dict_on_list_for_sort_func, test_fixture_dict_on_list_for_sort_func_correct_result_deposit_open
    ):
    search_string = 'Открытие вклада'
    assert (sort_by_search_string
            (test_fixture_dict_on_list_for_sort_func, search_string)
            ) == test_fixture_dict_on_list_for_sort_func_correct_result_deposit_open

def test_sort_by_search_string_incoming_type_list():
    with pytest.raises(ValueError) as exc_info:
        sort_by_search_string({}, 'Открытие вклада')
        assert str(exc_info.value) == "Не верный тип данных или список транзакций отсутствует"


def test_sort_by_search_string_empty_list():
    with pytest.raises(ValueError) as exc_info:
        sort_by_search_string([], 'Открытие вклада')
        assert str(exc_info.value) == "Не верный тип данных или список транзакций отсутствует"


def test_sort_by_search_string_empty_search_string(test_fixture_dict_on_list_for_sort_func):
    with pytest.raises(ValueError) as exc_info:
        sort_by_search_string(test_fixture_dict_on_list_for_sort_func, '')
        assert str(exc_info.value) == "Не верный тип данных или строка поиска пуста или отсутствует"

def test_sort_by_search_string_incoming_type_search_string(test_fixture_dict_on_list_for_sort_func):
    with pytest.raises(ValueError) as exc_info:
        sort_by_search_string(test_fixture_dict_on_list_for_sort_func, ['Открытие вклада'])
        assert str(exc_info.value) == "Не верный тип данных или строка поиска пуста или отсутствует"

def test_sort_by_category_all(test_fixture_dict_on_list_for_sort_func):
    assert sort_by_category(test_fixture_dict_on_list_for_sort_func,
        ['Открытие вклада', 'Перевод с карты на карту', 'Перевод организации']
    ) == {'Перевод организации': 1, 'Перевод с карты на карту': 2, 'Открытие вклада': 1}


def test_sort_by_category_only_transfer(test_fixture_dict_on_list_for_sort_func):
    assert sort_by_category(test_fixture_dict_on_list_for_sort_func,
        ['Перевод организации']
    ) == {'Перевод организации': 1}


def test_sort_by_category_invalid_type_list(test_fixture_dict_on_list_for_sort_func):
    with pytest.raises(ValueError) as exc_info:
        sort_by_category({}, ['Перевод организации'])
        assert str(exc_info.value) == "Не верный тип данных или список транзакций отсутствует"


def test_sort_by_category_invalid_type_category(test_fixture_dict_on_list_for_sort_func):
    with pytest.raises(ValueError) as exc_info:
        sort_by_category(test_fixture_dict_on_list_for_sort_func, {})
        assert str(exc_info.value) == "Не верный тип данных или список категорий отсутствует"