from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date, sort_by_search_string
from src.settings import CSV_FILE, JSON_FILE, XLSX_FILE
from src.transactions_processing import processing_csv, processing_excel
from src.utils import processing_json_dict
from src.widget import get_date, mask_account_card


def main():
    """Основная функция проекта, обрабатывающая запросы пользователя
    по фильтрации пользовательских транзакций и их вывода"""

    print(
        "Добро пожаловать в программу работы с банковскими транзакциями."
        "Выберите необходимый пункт меню:\n 1. Получить информацию о транзакциях из JSON-файла\n "
        "2. Получить информацию о транзакциях из CSV-файла\n "
        "3. Получить информацию о транзакциях из XLSX-файла"
    )

    while True:
        user_input = input("Введите номер выбранного Вами раздела меню (1/2/3): ")
        user_input = int(user_input)
        if user_input == 1:
            print("Для обработки выбран JSON-файл.")
            input_welcome = 1
            break
        elif user_input == 2:
            print("Для обработки выбран CSV-файл.")
            input_welcome = 2
            break
        elif user_input == 3:
            print("Для обработки выбран XLSX-файл.")
            input_welcome = 3
            break
        else:
            print("Выберете один из пунктов меню.")

    while True:
        user_input = input(
            "Введите статус, по которому необходимо выполнить фильтрацию."
            "Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING. Введите: "
        )
        if user_input.lower() == "executed":
            print('Операции отфильтрованы по статусу "EXECUTED"')
            status_for_operation = "EXECUTED"
            break
        elif user_input.lower() == "canceled":
            print('Операции отфильтрованы по статусу "CANCELED"')
            status_for_operation = "CANCELED"
            break
        elif user_input.lower() == "pending":
            print('Операции отфильтрованы по статусу "PENDING"')
            status_for_operation = "PENDING"
            break
        else:
            print(f"Статус операции {user_input} недоступен.")

    list_of_parameters_1 = []
    print("Отсортировать операции по дате?")
    while True:
        user_input_data = input("Введите Да или Нет: ")
        if user_input_data.lower() == "да":
            list_of_parameters_1.append("да")
            print("Отсортировать по возрастанию или по убыванию?")
            user_input_sort = input("Введите: ")
            if user_input_sort.lower() == "по возрастанию":
                list_of_parameters_1.append(True)
                break
            elif user_input_sort.lower() == "по убыванию":
                list_of_parameters_1.append(False)
                break
            else:
                print("Выберете один из предложенных пунктов: по возрастанию/по убыванию")
        elif user_input_data.lower() == "нет":
            break
        else:
            print("Вводите только Да или Нет")

    list_of_settings_by_currency = []
    print("Выводить только рублевые транзакции?")
    while True:
        user_input = input("Введите Да или Нет: ")
        if user_input.lower() == "да":
            list_of_settings_by_currency.append("RUB")
            break
        elif user_input.lower() == "нет":
            break
        else:
            print("Вводите только Да или Нет")

    list_of_settings_by_word = []
    print("Отфильтровать список транзакций по определенному слову в описании?")
    while True:
        user_input = input("Введите Да или Нет: ")
        if user_input.lower() == "да":
            user_input_word = input("Введите ключевое слово: ")
            list_of_settings_by_word.append(user_input_word.lower())
            break
        elif user_input.lower() == "нет":
            break
        else:
            print("Вводите только Да или Нет")

    func_json = processing_json_dict
    func_csv = processing_csv
    func_xlsx = processing_excel

    if input_welcome == 1:
        result_base = func_json(JSON_FILE)
    elif input_welcome == 2:
        result_base = func_csv(CSV_FILE)
    else:
        result_base = func_xlsx(XLSX_FILE)

    result_filter = filter_by_state(result_base, status_for_operation)

    if "да" in list_of_parameters_1:
        type_sort = list_of_parameters_1[0]
        result_filter = sort_by_date(result_filter, type_sort)

    if len(list_of_settings_by_currency) > 0:
        for x in list_of_settings_by_currency:
            if x == "RUB":
                type_currency = x
                filter_by_currency(result_filter, type_currency)

    if len(list_of_settings_by_word) > 0:
        word = list_of_settings_by_word[0]
        sort_by_search_string(result_filter, word)

    result = result_filter

    if not result:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    if result:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(result)}")

        if input_welcome == 1:
            for x in result_filter:
                date = get_date(x.get("date"))
                description = x.get("description")
                account_from = mask_account_card(x.get("from"))
                account_to = mask_account_card(x.get("to"))
                amount = x["operationAmount"]["amount"]
                currency = x["operationAmount"]["currency"]["code"]

                print(f"{date} {description} {account_from} -> {account_to} Сумма: {amount} {currency}")

        else:
            for x in result_filter:
                date = get_date(x.get("date"))
                description = x.get("description")
                account_from = mask_account_card(str(x.get("from")))
                account_to = mask_account_card(str(x.get("to")))
                amount = x.get("amount")
                currency = x.get("currency_code")

                print(f"{date} {description} {account_from} -> {account_to} Сумма: {amount} {currency}")


if __name__ == "__main__":
    main()
