from typing import Iterator


def filter_by_currency(incoming_list: list[dict[str, int, dict[str, int, dict, [str, int, dict, [str, int]]]]], currency_type: str = "USD") -> Iterator[
    dict[str, dict[str, int], int]]:
    """Функция, которая принимает на вход список словарей, представляющих транзакции.
Функция должна возвращать итератор, который поочередно выдает транзакции,
где валюта операции соответствует заданной (например, USD)."""

    for transaction in incoming_list:
        if transaction["operationAmount"]["currency"]["name"] == currency_type:
            yield transaction


def transaction_descriptions():
    pass


def card_number_generator():
    pass
