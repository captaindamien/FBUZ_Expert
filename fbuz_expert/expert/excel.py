import sqlite3
import openpyxl
import datetime

conn = sqlite3.connect("../db.sqlite3")
cursor = conn.cursor()


def date_search(d_from, d_after):
    sql = "SELECT * FROM expert_expertises WHERE created BETWEEN ? AND ?"
    cursor.execute(sql, (d_from, d_after))

    return change_data(cursor.fetchall())


def change_data(data):
    new_data = []
    for el in data:
        # меняем элементы местами под заголовки
        el_change = list(el)
        el_change.pop(0)
        el_change.insert(0, el_change.pop())
        el_change.pop(-1)
        el_change.pop(-1)
        new_data.append(tuple(el_change))

    return new_data


def excel_append():
    excel_file = openpyxl.load_workbook('../export/template.xlsx')
    excel_sheet = excel_file['Лист1']

    exp_list = date_search('2022-01-27', '2022-03-04')
    for row in exp_list:
        excel_sheet.append(row)

    excel_file.save('../export/new_template.xlsx')


excel_append()
