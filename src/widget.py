from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(incoming_data: str) -> str:
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
    else:
        final_masks_number += get_mask_account(numbers)

    return f"{text}{final_masks_number}"
