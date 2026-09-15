from dataclasses import field
from datetime import date
from typing import Optional

from models.novel import Novel


class Round:
    id_round: Optional[int] = field(default=None, init=False)
    number: int
    date_round: date
    ketps_novel: list[Novel]