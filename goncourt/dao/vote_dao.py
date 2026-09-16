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

    def remove_vote_for_year(self, cursor, year):
        sql = f"""DELETE FROM {self.get_table_name()}
                    WHERE {self.get_table_name()}.id_year = %(id_year)s
                    AND {self.get_table_name()}.id_novel NOT IN (
                        SELECT step.id_novel
                        FROM round
                        JOIN step ON step.id_round = round.id_round
                        WHERE round.id_year = %(id_year)s
                        AND round.number = (
                            SELECT MAX(number)
                            FROM round
                            WHERE id_year = %(id_year)s
                        )
                    );
            """
        cursor.execute(sql, {"id_year": year})
        return True

    def add_vote_for_year(self, cursor, year):
        sql = """INSERT INTO vote (number_of_vote, id_novel, id_year)
                    SELECT 0, step.id_novel, %(id_year)s
                    FROM step
                    JOIN round ON round.id_round = step.id_round
                    WHERE round.id_year = %(id_year)s
                      AND round.number = (
                          SELECT MAX(number)
                          FROM round
                          WHERE id_year = %(id_year)s
                      )
                      AND step.id_novel NOT IN (
                          SELECT id_novel
                          FROM vote
                          WHERE id_year = %(id_year)s
                      );"""
        cursor.execute(sql, {"id_year": year})
        return True