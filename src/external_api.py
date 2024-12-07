import os
from typing import Any

import requests
from dotenv import load_dotenv


def currency_conversion(incoming_transaction: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях, тип данных —
    float. Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли."""

    if not isinstance(incoming_transaction, dict):
        raise ValueError("Не верный тип данных входящей транзакции")

    elif (
        incoming_transaction["operationAmount"]["amount"] == "0"
        or incoming_transaction["operationAmount"]["amount"] == ""
    ):
        raise ValueError("Сумма транзакции равна нулю или отсутствует")

    elif incoming_transaction["operationAmount"]["currency"]["code"] == "":
        raise ValueError("Валюта транзакции не найдена")

    elif incoming_transaction["operationAmount"]["currency"]["code"] == "RUB":
        amount = float(incoming_transaction["operationAmount"]["amount"])
        return amount

    elif incoming_transaction["operationAmount"]["currency"]["code"] != "RUB":
        currency = incoming_transaction["operationAmount"]["currency"]["code"]
        amount = incoming_transaction["operationAmount"]["amount"]
        to = "RUB"

        load_dotenv()
        api = os.getenv("API_Key_ERD")

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={currency}&amount={amount}"
        payload: dict[str, Any] = {}
        headers = {"apikey": api}
        response = requests.request("GET", url, headers=headers, data=payload)
        status_code = response.status_code

        result = response.json()
        final_sum = round(float(result["result"]), 2)
        return final_sum
