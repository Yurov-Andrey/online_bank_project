from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(incoming_data: str) -> str:
    """Функция принимает номер карты или счета и маскирует его, в зависимости от принятых данных"""
    if not incoming_data:
        return ("Отсутствует номер счета или карты")

    numbers = ""
    text = ""
    final_masks_number = ""

    for symbol in incoming_data:
        if symbol.isdigit():
            numbers += symbol
        elif symbol.isalpha() or symbol == " ":
            text += symbol

    if len(numbers) == 16:
        final_masks_number += get_mask_card_number(numbers)
    elif len(numbers) == 20:
        final_masks_number += get_mask_account(numbers)
    else:
        return 'Нет данных (счет или карта отсутствуют)'

    return f"{text}{final_masks_number}"


def get_date(incoming_date: str) -> str:
    """Функция принимает строковые данные содержащие текущую дату и выводит в удобном формате"""
    date_string = ""

    if len(incoming_date) == 0:
        raise ValueError("Данные о дате отсутствуют")

    for i in incoming_date:
        if i.isdigit() and len(date_string) < 10:
            date_string += i
        elif i == "-" and len(date_string) < 10 or i == "." and len(date_string) < 10:
            date_string += "."

    final_date_string = date_string[8:11] + date_string[4:8] + date_string[0:4]

    return final_date_string
