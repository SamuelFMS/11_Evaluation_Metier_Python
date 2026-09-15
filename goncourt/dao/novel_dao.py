from dataclasses import dataclass
from typing import Optional

from pymysql.cursors import Cursor

from dao.dao import Dao
from models.novel import Novel


@dataclass
class NovelDao(Dao[Novel]):
    @classmethod
    def get_table_name(cls):
        return "novel"

    def map_record(self, record) -> Optional[Novel]:
        novel: Optional[Novel] = None
        if record is not None:
            novel = Novel(title=record["title"], summary=record["summary"], editor=record["editor"],
                          publication_date=record["publication_date"], number_of_pages=record["number_of_pages"],
                          ISBN=record["ISBN"], publisher_price=record["publisher_price"])

            novel.id_novel = record["id_novel"]
        return novel

    def add_novel_to_round(self, cursor: Cursor, novel_id: int, id_round: int) -> bool:
        sql = """INSERT INTO step(id_novel, id_round) VALUES (%s, %s)"""
        cursor.execute(sql, (novel_id, id_round))
        return cursor.lastrowid is not None
