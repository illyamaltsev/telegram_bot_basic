# -*- coding: utf-8 -*-

from enum import Enum

token = '749710534:AAHW9BNMfrZR2RD3p8neuKeuovR1JpOOsKM'
db_file = "database.vdb"


class States(Enum):
    """
    Мы используем БД Vedis, в которой хранимые значения всегда строки,
    поэтому и тут будем использовать тоже строки (str)
    """
    S_START = "0"  # Начало нового диалога
    S_ENTER_NAME = "1"
    S_ENTER_AGE = "2"
    S_SEND_PIC = "3"
