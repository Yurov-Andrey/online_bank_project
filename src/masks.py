def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номера принимаемых карт"""
    if len(card_number) != 16:
        raise ValueError("Не верная длина номера карты")

    if not card_number.isdigit():
        raise ValueError("Номер карты должен состоять только из цифр")

    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[12:16]}"


def get_mask_account(account_number: str) -> str:
    """Функция маскирует номера принимаемых счетов"""
    if len(account_number) != 20:
        raise ValueError("Не верная длина номера счета")

    if not account_number.isdigit():
        raise ValueError("Номер счета должен состоять только из цифр")

    return f"**{account_number[-5:]}"
