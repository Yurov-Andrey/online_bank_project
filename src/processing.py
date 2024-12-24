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

    final_list = []
    for nested_dict in incoming_list:
        values_list = nested_dict.values()

        for word in values_list:
            string = word
            pattern = search_string
            result = re.search(pattern, string, flags=re.IGNORECASE)
            if result != None:
                final_list.append(nested_dict)
            else:
                return f'Указанные операциии не найдены'

    return final_list


def sort_by_category(incoming_list: list[dict], category_list: list) -> dict:
    """Функция, которая будет принимать список словарей с данными о банковских операциях и список категорий операций,
а возвращать словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""

    check_list = []

    for nested_dict in incoming_list:
        values_list = nested_dict.values()
        for word in values_list:
            string = word
            for category in category_list:
                pattern = category
                result = re.search(pattern, string, flags=re.IGNORECASE)
                if result != None:
                    check_list.append(category)

    count_dict = dict(Counter(check_list))

    return count_dict


if __name__ == '__main__':
    my_list = [
        {'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210', 'currency_name': 'Sol',
         'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
         'description': 'Перевод организации'},
        {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z',
         'amount': '29740', 'currency_name': 'Peso', 'currency_code': 'COP',
         'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643',
         'description': 'Перевод с карты на карту'},
        {'id': '593027', 'state': 'CANCELED',
         'date': '2023-07-22T05:02:01Z',
         'amount': '30368',
         'currency_name': 'Shilling',
         'currency_code': 'TZS',
         'from': 'Visa 1959232722494097',
         'to': 'Visa 6804119550473710',
         'description': 'Перевод с карты на карту'},
        {'id': '5380041',
         'state': 'CANCELED',
         'date': '2021-02-01T11:54:58Z',
         'amount': '23789',
         'currency_name': 'Peso',
         'currency_code': 'UYU',
         'from': '',
         'to': 'Счет 23294994494356835683',
         'description': 'Открытие вклада'}
    ]

    my_category_list = ['Открытие вклада', 'Перевод с карты на карту', 'Перевод организации']
    print(sort_by_category(my_list, my_category_list))
