from abc import ABC
from dataclasses import dataclass
from typing import ClassVar

import pymysql


@dataclass
class Business[T](ABC):
    __connection: ClassVar[pymysql.Connection | None] = None

    @classmethod
    def set_connection(cls, database: str, user: str):
        if cls.__connection is None:
            cls.__connection = pymysql.connect(
                host="localhost",
                user=user,
                database=database,
                cursorclass=pymysql.cursors.DictCursor
            )

    @classmethod
    def get_connection(cls) -> pymysql.Connection:
        if cls.__connection is None:
            cls.__connection = pymysql.connect(
                host="localhost",
                user="Goncourt",
                database="goncourt",
                cursorclass=pymysql.cursors.DictCursor
            )
        assert cls.__connection is not None
        return cls.__connection