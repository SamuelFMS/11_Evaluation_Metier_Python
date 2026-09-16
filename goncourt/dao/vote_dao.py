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
