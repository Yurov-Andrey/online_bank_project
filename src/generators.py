# from typing import Generator, Iterator


# def filter_by_currency(incoming_list: list[dict], currency_type: str) -> Iterator[dict]:
def filter_by_currency(incoming_list: list, currency_type: str):
    """Функция, которая принимает на вход список словарей, представляющих транзакции.
    Функция должна возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)."""

    for transaction in incoming_list:
        if "operationAmount" not in transaction:
            raise ValueError("Не найдено значение 'operationAmount'")

        elif "currency" not in transaction["operationAmount"]:
            raise ValueError("Не найдено значение 'currency'")

        elif "code" not in transaction["operationAmount"]["currency"]:
            raise ValueError("Не найдено значение 'code'")

    for transaction in incoming_list:
        if transaction["operationAmount"]["currency"]["code"] == currency_type:
            yield transaction


# def transaction_descriptions(incoming_list: list[dict]) -> Generator[dict]:
def transaction_descriptions(incoming_list: list):
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""

    if not isinstance(incoming_list, list) or len(incoming_list) == 0:
        raise ValueError("Не верный тип данных или список транзакций отсутствует")

    for transaction in incoming_list:
        if "description" not in transaction or transaction["description"] == "":
            raise ValueError("Не найдено значение 'description'")

        yield transaction["description"]


# def card_number_generator(start: int = 1, end: int = 20) -> Generator[str]:
def card_number_generator(start: int = 1, end: int = 20):
    """Функция генерирует номера карт в заданном диапазоне и выдаёт в корректном формате"""

    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("Не верный тип данных входящих аргументов")

    if start > end:
        raise ValueError("Не верно заданы параметры start и stop, start должен быть меньше или равен stop")

    if len(str(start)) > 16 or len(str(end)) > 16:
        raise ValueError(
            "Слишком большое число передано в start/end, максимальная длина строки не должна превышать 16 символов"
        )

    while start <= end:
        formatted_number = f"{start:016}"
        formatted_number = " ".join([formatted_number[i : i + 4] for i in range(0, len(formatted_number), 4)])
        yield formatted_number
        start += 1
