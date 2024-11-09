def filter_by_state(incoming_list: list[dict]) -> list[dict]:
    filtered_list = []
    for any_dict in incoming_list:
        for key, value in any_dict.items():
            if value == 'EXECUTED':
                filtered_list.append(any_dict)

    return filtered_list


def sort_by_date(incoming_list: list[dict], sorting_order = True) -> list[dict]:
    sort_dictionary = sorted(incoming_list, key=lambda x: x['date'], reverse = sorting_order)

    return sort_dictionary


random_dict = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
               {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
               {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
               {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

print(filter_by_state(random_dict))
print(sort_by_date(random_dict))
