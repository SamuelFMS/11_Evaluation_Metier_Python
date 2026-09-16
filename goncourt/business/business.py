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
        Set a connection to the database
        :param database: name of the database
        :param user: name of the user
        :return:
        """
        if cls.__connection is not None:
            cls.__connection.close()

        cls.__connection = pymysql.connect(
            host="localhost",
            user=user,
            database=database,
            cursorclass=pymysql.cursors.DictCursor
        )

    @classmethod
    def get_connection(cls) -> pymysql.Connection:
        """
        Get a connection to the database
        :return:
        """
        if cls.__connection is None:
            raise RuntimeError("La connexion à la base de données n'a pas été initialisée.")

        return cls.__connection

    @classmethod
    def close_connection(cls):
        """
        Close the connection to the database
        :return:
        """
        if cls.__connection is not None:
            cls.__connection.close()
            cls.__connection = None
