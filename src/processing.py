import re
from collections import Counter


def filter_by_state(incoming_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению"""

    filtered_list = []
    for unpacked_dictionary in incoming_list:
        for key, value in unpacked_dictionary.items():
            if key == "state" and value == state:
                filtered_list.append(unpacked_dictionary)

    return filtered_list


def sort_by_date(incoming_list: list[dict], sorting_order: bool = True) -> list[dict]:
    """Функция должна возвращать новый список, отсортированный по дате (date)"""

    sort_dictionary = sorted(incoming_list, key=lambda x: x["date"], reverse=sorting_order)

    return sort_dictionary


def sort_by_search_string(incoming_list: list[dict], search_string: str) -> list[dict]:
    """Функция, которая принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка."""

    if not isinstance(incoming_list, list) or len(incoming_list) == 0:
        raise ValueError("Не верный тип данных или список транзакций отсутствует")

    if not isinstance(search_string, str) or len(search_string) == 0:
        raise ValueError("Не верный тип данных или строка поиска пуста или отсутствует")

    final_list = []
    for nested_dict in incoming_list:
        values_list = nested_dict.values()

        for word in values_list:
            string = word
            pattern = search_string
            result = re.search(pattern, string, flags=re.IGNORECASE)
            if result is not None:
                final_list.append(nested_dict)

    return final_list


def sort_by_category(incoming_list: list[dict], category_list: list) -> dict:
    """Функция, которая будет принимать список словарей с данными о банковских операциях и список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    """

    if not isinstance(incoming_list, list) or len(incoming_list) == 0:
        raise ValueError("Не верный тип данных или список транзакций отсутствует")

    if not isinstance(category_list, list) or len(category_list) == 0:
        raise ValueError("Не верный тип данных или список категорий отсутствует")

    check_list = []

    for nested_dict in incoming_list:
        values_list = nested_dict.values()
        for word in values_list:
            string = word
            for category in category_list:
                pattern = category
                result = re.search(pattern, string, flags=re.IGNORECASE)
                if result is not None:
                    check_list.append(category)

    count_dict = dict(Counter(check_list))

    return count_dict
