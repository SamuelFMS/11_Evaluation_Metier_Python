from typing import Optional

from pymysql.cursors import Cursor

from dao.dao import Dao
from dao.novel_dao import NovelDao
from models.person import Person


class PersonDao(Dao[Person]):
    @classmethod
    def get_table_name(cls):
        return "person"

    def map_record(self, record) -> Optional[Person]:
        person: Optional[Person] = None
        if record is not None:
            person = Person(lastname=record["lastname"], firstname=record["firstname"],
                            biography=record["biography"])

            person.id_person = record["id_person"]
        return person
