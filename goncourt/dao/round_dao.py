from dataclasses import dataclass
from typing import Optional

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
            _round = Round(number=record["number"], date_round=record["date_"])
            _round.id_round = record["id_round"]
        return _round
