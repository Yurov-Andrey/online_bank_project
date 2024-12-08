import json
import logging
import os
from typing import Any

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(f"{log_dir}/utils.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(lineno)d: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def processing_json_dict(file_path: Any) -> list | str:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей
    с данными о финансовых транзакциях. Если файл пустой, содержит не список или не найден,
    функция возвращает пустой список."""

    try:
        logger.info(f"Старт работы функции {processing_json_dict}, принят файл по пути {file_path}")
        with open(file_path, "r", encoding="utf-8") as file:
            contents = json.load(file)
            logger.info(f"Открыт и прочитан файл {file}")

            logger.debug(f"Проверка типа данных содержимого файла.")
            if not isinstance(contents, list):
                empty_list: list = []
                logger.warning(
                    f"Проверка не пройдена, содержимое не является списком. Создан пустой список {empty_list}"
                )
                return empty_list

            elif len(contents) == 0:
                empty_list = []
                logger.warning(
                    f"Проверка не пройдена, содержимое является пустым списком. Создан пустой список {empty_list}"
                )
                return empty_list

            else:
                logger.info(f"Функция {processing_json_dict} завершила работу и вернула результат.")
                return contents

    except FileNotFoundError:
        logger.error(f"Запрашиваемый файл не найден или указан некорректный путь ({file_path}) к файлу")
        return f"Запрашиваемый файл не найден или указан некорректный путь ({file_path}) к файлу"

    except json.JSONDecodeError as e:
        empty_list = []
        logger.error(f"Ошибка {e}. Создан пустой список {empty_list}")
        return empty_list
