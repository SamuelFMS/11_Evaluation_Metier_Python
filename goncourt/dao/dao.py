from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

from pymysql.cursors import Cursor


@dataclass
class Dao[T](ABC):
    """Base class providing common database access operations for entities."""

    @classmethod
    @abstractmethod
    def get_table_name(cls) -> str:
        """
        Return the name of the database table associated with this DAO.

        :return: The database table name.
        """
        pass

    @abstractmethod
    def map_record(self, record) -> T:
        """
        Convert a database record into the corresponding entity.

        :param record: The database record to convert.
        :return: The entity created from the record.
        """
        pass

    def get_all(self, cursor: Cursor) -> list[T]:
        """
        Retrieve all entities from the associated database table.

        :param cursor: Database cursor used to execute the query.
        :return: A list containing all retrieved entities.
        """
        list_of_all: list[T] = []
        sql = f"SELECT * FROM {self.get_table_name()}"
        cursor.execute(sql)

        for record in cursor.fetchall():
            entity: Optional[T] = self.map_record(record)
            if entity is not None:
                list_of_all.append(entity)

        return list_of_all

    def get_by_id(self, cursor: Cursor, id: int) -> Optional[T]:
        """
        Retrieve an entity by its identifier.

        :param cursor: Database cursor used to execute the query.
        :param id: Identifier of the entity to retrieve.
        :return: The corresponding entity, or None if it does not exist.
        """
        sql = f"""
        SELECT * FROM {self.get_table_name()}
        WHERE id_{self.get_table_name()}=%s
        """
        cursor.execute(sql, (id,))
        record = cursor.fetchone()

        if record is None:
            return None

        return self.map_record(record)

    def get_by_related_id(
        self,
        cursor: Cursor,
        dao: "Dao",
        id_of_dao: int
    ) -> Optional[T]:
        """
        Retrieve an entity associated with an entity from another table.

        The relationship is determined using the identifier of the related
        entity.

        :param cursor: Database cursor used to execute the query.
        :param dao: DAO representing the related table.
        :param id_of_dao: Identifier of the related entity.
        :return: The associated entity, or None if no entity is found.
        """
        sql = f"""
        SELECT {self.get_table_name()}.*
        FROM {self.get_table_name()}
        JOIN {dao.get_table_name()}
        ON {dao.get_table_name()}.id_{self.get_table_name()}
            = {self.get_table_name()}.id_{self.get_table_name()}
        WHERE {dao.get_table_name()}.id_{dao.get_table_name()}=%s
        """
        cursor.execute(sql, (id_of_dao,))
        record = cursor.fetchone()

        if record is None:
            return None

        return self.map_record(record)

    def get_all_by_related_id(
        self,
        cursor: Cursor,
        related_dao: "Dao",
        related_id: int
    ) -> list[T]:
        """
        Retrieve all entities associated with an entity from another table.

        :param cursor: Database cursor used to execute the query.
        :param related_dao: DAO representing the related table.
        :param related_id: Identifier of the related entity.
        :return: A list containing all associated entities.
        """
        entities: list[T] = []

        sql = f"""
        SELECT {self.get_table_name()}.*
        FROM {self.get_table_name()}
        JOIN {related_dao.get_table_name()}
        ON {related_dao.get_table_name()}.id_{related_dao.get_table_name()}
            = {self.get_table_name()}.id_{related_dao.get_table_name()}
        WHERE {related_dao.get_table_name()}.id_{related_dao.get_table_name()}=%s
        """
        cursor.execute(sql, (related_id,))

        for record in cursor.fetchall():
            entity: Optional[T] = self.map_record(record)
            if entity is not None:
                entities.append(entity)

        return entities