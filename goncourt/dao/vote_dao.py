from dataclasses import dataclass
from typing import Optional

from dao.dao import Dao
from models.vote import Vote


@dataclass
class VoteDao(Dao[Vote]):
    @classmethod
    def get_table_name(cls):
        return "vote"

    def map_record(self, record) -> Optional[Vote]:
        vote: Optional[Vote] = None
        if record is not None:
            vote = Vote(number_of_votes=record["number_of_vote"], novel_id=record["id_novel"])
            vote.id_vote = record["id_vote"]
        return vote

    def remove_vote_for_year(self, cursor, id_novel: int, year: int):
        """
        Remove unused vote for the given year.
        :param cursor:
        :param year:
        :return:
        """
        sql = f"""DELETE FROM {self.get_table_name()}
                    WHERE {self.get_table_name()}.id_year = %(id_year)s AND {self.get_table_name()}.id_novel = %(id_novel)s
            """
        cursor.execute(sql, {"id_year": year, "id_novel": id_novel})
        return True

    def add_vote_for_year(self, cursor, id_novel: int, year: int):
        """
        Adding vote to the year
        :param cursor:
        :param year:
        :return:
        """
        sql = """INSERT INTO vote (number_of_vote, id_novel, id_year) VALUES (0, %s, %s)"""
        cursor.execute(sql, (id_novel, year))
        return True

    def update_note(self, cursor, vote: Vote):
        """
        Update the note for the given vote.
        :param cursor:
        :param vote:
        :return:
        """
        sql = f"""UPDATE {self.get_table_name()}
                SET number_of_vote = %(number_of_vote)s
                WHERE {self.get_table_name()}.{self.get_primary_key()} = %(id_novel)s"""
        cursor.execute(sql, {"number_of_vote": vote.number_of_votes, "id_novel": vote.id_vote})
        return cursor.rowcount == 1
