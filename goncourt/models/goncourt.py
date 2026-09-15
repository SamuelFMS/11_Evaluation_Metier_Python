from dataclasses import dataclass, field
from typing import List

from models.vote import Vote

@dataclass
class Goncourt:
    year: int
    votes: list[Vote] = field(default_factory=list, init=False)