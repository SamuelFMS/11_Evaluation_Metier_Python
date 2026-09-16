from dataclasses import dataclass
from typing import Optional

from pymysql import cursors
from pymysql.cursors import Cursor

from dao.dao import Dao
from models.round import Round


@dataclass
class RoundDao(Dao[Round]):
    @classmethod
    def get_table_name(cls):
        return "round"

    def map_record(self, record) -> Optional[Round]:
        _round: Optional[Round] = None
        if record is not None:
            _round = Round(date_round=record["date_"], id_round_parent=record["id_round_parent"])
            _round.id_round = record["id_round"]
        return _round

    def get_number(self, cursor: Cursor, id_round:int) -> Optional[int]:
        sql = """
        WITH RECURSIVE round_hierarchy AS (
            -- Étape de base
            SELECT
                r.id_round,
                1 AS number
            FROM round r
            WHERE r.id_round_parent is NULL
        
            UNION ALL
        
            -- Étape récursive : on remonte vers le parent
            SELECT
                r.id_round,
                rh.number + 1
            FROM round_hierarchy rh
            JOIN round r
            ON r.id_round_parent = rh.id_round
        )
        SELECT *
        FROM round_hierarchy
        WHERE id_round = %s;
        """
        cursor.execute(sql, id_round)
        record = cursor.fetchone()

        if record is None:
            return None

        return record["number"]

    def get_max_round_number(self, cursor: Cursor, id_year:int) -> int:
        sql = """
        WITH RECURSIVE round_hierarchy AS (
            -- Étape de base
            SELECT
                r.id_round,
                1 AS number
            FROM round r
            WHERE r.id_round_parent is NULL AND r.id_year = %(id_year)s
        
            UNION ALL
        
            -- Étape récursive : on remonte vers le parent
            SELECT
                r.id_round,
                rh.number + 1
            FROM round_hierarchy rh
            JOIN round r
            ON r.id_round_parent = rh.id_round
    		WHERE r.id_year = %(id_year)s
        )
        SELECT max(number) as number
        FROM round_hierarchy
        """
        cursor.execute(sql, {"id_year": id_year})
        record = cursor.fetchone()
        assert record
        return record["number"]