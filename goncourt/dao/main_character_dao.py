from dataclasses import dataclass
from typing import Optional

from dao.dao import Dao
from models.main_character import MainCharacter


@dataclass
class MainCharacterDao(Dao[MainCharacter]):
    @classmethod
    def get_table_name(cls):
        return "main_character"

    def map_record(self, record) -> Optional[MainCharacter]:
        main_character: Optional[MainCharacter] = None
        if record is not None:
            main_character = MainCharacter(name=record["name"])

            main_character.id_main_character = record["id_main_character"]
        return main_character
