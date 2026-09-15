from dataclasses import field
from typing import Optional

from models.novel import Novel


class Vote:
    id_vote: Optional[int] = field(default=None, init=False)
    number_of_votes: int
    novel: Novel