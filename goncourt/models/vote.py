from dataclasses import field, dataclass
from typing import Optional

from models.novel import Novel


@dataclass
class Vote:
    id_vote: Optional[int] = field(default=None, init=False)
    number_of_votes: int
    novel_id: int
    novel: Optional[Novel] = field(default=None, init=False)
