def filter_by_state(incoming_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению"""
    filtered_list = []
    for any_dict in incoming_list:
        for key, value in any_dict.items():
            if value == state:
                filtered_list.append(any_dict)

    return filtered_list


def sort_by_date(incoming_list: list[dict], sorting_order: bool = True) -> list[dict]:
    """Функция должна возвращать новый список, отсортированный по дате (date)"""
    sort_dictionary = sorted(incoming_list, key=lambda x: x["date"], reverse=sorting_order)

    return sort_dictionary
