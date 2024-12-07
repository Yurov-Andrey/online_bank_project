import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(lineno)d: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номера принимаемых карт"""

    try:
        logger.info(f"Старт работы функции {get_mask_card_number}")
        if len(card_number) != 16:
            logger.debug(f"Проверяем длину строки {card_number}.")
            raise ValueError("Не верная длина номера карты")

        if not card_number.isdigit():
            logger.debug(f"Проверяем состоит ли строка {card_number} только из цифр.")
            raise ValueError("Номер карты должен состоять только из цифр")

        logger.info(f"Функция {get_mask_account} завершила работу и вернула результат.")
        return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:16]}"

    except ValueError as e:
        logger.error(f"Возникла ошибка: {e}")


def get_mask_account(account_number: str) -> str:
    """Функция маскирует номера принимаемых счетов"""

    try:
        logger.info(f"Старт работы функции {get_mask_account}")
        if len(account_number) != 20:
            logger.debug(f"Проверяем длину строки {account_number}.")
            raise ValueError("Не верная длина номера счета")

        if not account_number.isdigit():
            logger.debug(f"Проверяем состоит ли строка {account_number} только из цифр.")
            raise ValueError("Номер счета должен состоять только из цифр")

        logger.info(f"Функция {get_mask_account} завершила работу и вернула результат.")
        return f"**{account_number[-5:]}"

    except ValueError as e:
        logger.error(f"Возникла ошибка: {e}")
