from abc import ABC
from dataclasses import dataclass
from typing import ClassVar

import pymysql


@dataclass
class Business[T](ABC):
    __connection: ClassVar[pymysql.Connection | None] = None

    @classmethod
    def set_connection(cls, database: str, user: str):
        """
        Initializes the database connection with specific credentials.
        The connection is only created if it does not already exist.
        :param database: name of the database
        :param user: name of the user of the database
        :return:
        """
        if cls.__connection is None:
            cls.__connection = pymysql.connect(host="localhost", user=user, database=database,
                cursorclass=pymysql.cursors.DictCursor)

    @classmethod
    def get_connection(cls) -> pymysql.Connection:
        """
        Retrieves the active connection or creates a default one if none exists.
        :return: return the connection
        """
        if cls.__connection is None:
            cls.__connection = pymysql.connect(host="localhost", user="Goncourt", database="goncourt",
                cursorclass=pymysql.cursors.DictCursor)
        assert cls.__connection is not None
        return cls.__connection
