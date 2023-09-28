import os.path
import pandas as pd
from R4C.settings import BASE_DIR

COLUMNS_NAME = {'Модель': 'model', 'Версия': 'version', 'Количество за неделю': 'rcount'}
PATH_TEMP_FILE = os.path.join(BASE_DIR, 'robots', 'temp_files', 'robots.xlsx')


def to_excel(records: list):
    """
    Формирует DataFrame и записывает в файл по пути PATH_TEMP_FILE .
    :param records:  список записей из бд
    :return: None
    """
    tables = {}
    for record in records:
        try:
            for name, key in COLUMNS_NAME.items():
                tables[record['model']][name].append(record[key])
        except KeyError:
            tables[record['model']] = {}
            for name, key in COLUMNS_NAME.items():
                tables[record['model']][name] = [record[key]]
    writer = pd.ExcelWriter(PATH_TEMP_FILE)
    for sheet_name, table in tables.items():
        df = pd.DataFrame(table)
        df.to_excel(writer, sheet_name=sheet_name)
    writer.close()


