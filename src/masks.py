import logging
import os

from src.settings import REPORTS_PATH

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(f"{REPORTS_PATH}/masks.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(lineno)d: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номера принимаемых карт"""

    logger.info(f"Старт работы функции {get_mask_card_number}")
    if len(card_number) != 16:
        logger.debug(f"Проверяем длину строки {card_number}.")
        logger.error("Не верная длина номера карты")
        raise ValueError("Не верная длина номера карты")

    if not card_number.isdigit():
        logger.debug(f"Проверяем состоит ли строка {card_number} только из цифр.")
        logger.error("Номер карты должен состоять только из цифр")
        raise ValueError("Номер карты должен состоять только из цифр")

    masked_card_number = f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:16]}"
    logger.info(f"Функция завершила работу и вернула результат: {masked_card_number}")
    return masked_card_number


def get_mask_account(account_number: str) -> str:
    """Функция маскирует номера принимаемых счетов"""

    logger.info(f"Старт работы функции {get_mask_account}")
    if len(account_number) != 20:
        logger.debug(f"Проверяем длину строки {account_number}.")
        logger.error("Не верная длина номера счета")
        raise ValueError("Не верная длина номера счета")

    if not account_number.isdigit():
        logger.debug(f"Проверяем состоит ли строка {account_number} только из цифр.")
        logger.error("Номер счета должен состоять только из цифр")
        raise ValueError("Номер счета должен состоять только из цифр")

    masked_account_number = f"**{account_number[-5:]}"
    logger.info(f"Функция завершила работу и вернула результат: {masked_account_number}")
    return masked_account_number
