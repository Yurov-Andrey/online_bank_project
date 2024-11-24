from typing import Generator, Iterator


def filter_by_currency(incoming_list: list[dict], currency_type: str = "USD") -> Iterator[dict]:
    """Функция, которая принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""

    if not isinstance(incoming_list, list):
        raise ValueError("Не верный тип данных входящих аргументов")

    for transaction in incoming_list:
        if transaction["operationAmount"] not in transaction:
            raise ValueError("Не найдено значение 'operationAmount'")

        elif transaction["operationAmount"]["currency"] not in transaction["operationAmount"]:
            raise ValueError("Не найдено значение 'currency'")

        elif transaction["operationAmount"]["currency"]["name"] not in transaction["operationAmount"]["currency"]:
            raise ValueError("Не найдено значение 'name'")

        elif transaction["operationAmount"]["currency"]["name"] != currency_type:
            raise ValueError("Валюта транзакции не соответствует currency_type")

    for transaction in incoming_list:
        if transaction["operationAmount"]["currency"]["name"] == currency_type:
            yield transaction


def transaction_descriptions(incoming_list: list[dict]) -> Generator[list[dict]]:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""

    if not isinstance(incoming_list, list):
        raise ValueError("Не верный тип данных входящих аргументов")

    for transactions in incoming_list:
        if transactions["description"] not in transactions or transactions["description"] == "":
            raise ValueError("Не найдено значение 'description' или список транзакций отсутствует")

    for transactions in incoming_list:
        yield transactions["description"]


def card_number_generator(start: int = 1, end: int = 20) -> Generator[str]:
    """Функция генерирует номера карт в заданном диапазоне и выдаёт в корректном формате"""

    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Не верный тип данных входящих аргументов")

    if start > end:
        raise ValueError("Не верно заданы параметры start и stop, start должен быть меньше или равен stop")

    if len(str(end)) > 16:
        raise ValueError(
            "Слишком большое число передано в end, максимальная длина строки не должна превышать 16 символов"
        )

    while start <= end:
        formatted_number = f"{start:016}"
        formatted_number = " ".join([formatted_number[i:i + 4] for i in range(0, len(formatted_number), 4)])
        yield formatted_number
        start += 1
