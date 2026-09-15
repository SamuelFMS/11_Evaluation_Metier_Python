from dataclasses import dataclass
from typing import Optional

from dao.dao import Dao
from models.goncourt import Goncourt


@dataclass
class GoncourtDao(Dao[Goncourt]):
    def get_primary_key(self):
        return "id_year"
    @classmethod
    def get_table_name(cls):
        return "goncourt"

    def map_record(self, record) -> Optional[Goncourt]:
        goncourt: Optional[Goncourt] = None
        if record is not None:
            goncourt = Goncourt(year=record["id_year"],)
        return goncourt