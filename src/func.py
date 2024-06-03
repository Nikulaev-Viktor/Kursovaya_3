import json
from datetime import datetime


def json_encode():
    """Преобразуем json файл в Python формат"""
    with open("operations.json", encoding="utf-8") as f:
        data = json.load(f)
        return data


def last_five_operations(data):
    """Сортируем и выводим пять последних операций"""
    new_operation = [operation for operation in data if "state" in operation and operation["state"] == "EXECUTED"] 
    sorted_operations = sorted(new_operation, key=lambda x: x["date"], reverse=True)
    return sorted_operations[:4]
    # for operations in data:
    #     if "state" in operations and operations["state"] == "EXECUTED":
    #         new_operation.append(operations)
    # sorted_operations = sorted(new_operation, key=lambda x: x["date"], reverse=True)
    # return sorted_operations[-3:]

# Не работает, выводит либо 4, либо 6


def format_date(date):
    """"Переводим дату в формат ДД.ММ.ГГГГ"""
    date_format = date.split("T")[0].split("-")[::-1]
    return ".".join(date_format)


def format_card(card):
    card = card.split()
    card_number = card.pop()
    card_name = " ".join(card)
    if card_name.lower() == "счет":
        number_secret = "** " + card_number[-4:]
    else:
        number_secret = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return f"{card_name} {number_secret}"


def get_data_format(data):
    """"Форматируем данные под ТЗ"""
    for operation in data:
        if "from" in operation:
            date = format_date(operation["date"])
            operation_a = operation["description"]
            from_who = format_card(operation["from"])
            to_who = format_card(operation["to"])
            sum_trans = operation["operationAmount"]["amount"]
            currency = operation["operationAmount"]["currency"]["name"]
            print(f"{date} {operation_a}\n{from_who} -> {to_who}\n{sum_trans} {currency}")
        else:
            pass
