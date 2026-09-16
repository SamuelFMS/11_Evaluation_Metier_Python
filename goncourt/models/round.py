from dataclasses import field, dataclass
from datetime import date
from typing import Optional


@dataclass
class Round:
    id_round: Optional[int] = field(default=None, init=False)
    date_round: date
    id_round_parent: Optional[int]