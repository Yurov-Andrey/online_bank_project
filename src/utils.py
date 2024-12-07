import json
import logging
from typing import Any

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(lineno)d: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def processing_json_dict(file_path: Any) -> list | str:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список."""

    try:
        logger.info(f"Старт работы функции {processing_json_dict}")
        with open(file_path, "r", encoding="utf-8") as file:
            contents = json.load(file)
            logger.info(f"Открыт и прочитан файл {file_path}")

            logger.debug(f'Проверка типа данных содержимого файла {file_path}')
            if not isinstance(contents, list):
                empty_list: list = []
                logger.warning(f'Проверка не пройдена, создан пустой список {empty_list}')
                return empty_list


            elif len(contents) == 0:
                logger.debug(f'Проверка типа данных содержимого файла {file_path}')
                empty_list = []
                return empty_list

            else:
                return contents

    except FileNotFoundError:
        return f"Запрашиваемый файл не найден или указан некорректный путь ({file_path}) к файлу"

    except json.JSONDecodeError:
        empty_list = []
        return empty_list
