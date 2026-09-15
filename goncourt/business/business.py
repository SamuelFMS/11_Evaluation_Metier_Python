from abc import ABC
from dataclasses import dataclass
from typing import ClassVar

import pymysql


@dataclass
class Business[T](ABC):
    connection: ClassVar[pymysql.Connection] = \
        pymysql.connect(host='localhost',
                        user='Goncourt',
                        database='goncourt',
                        cursorclass=pymysql.cursors.DictCursor)