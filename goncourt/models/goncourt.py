from dataclasses import dataclass, field
from typing import List

from models.round import Round
from models.vote import Vote

@dataclass
class Goncourt:
    year: int
    rounds: list[Round] = field(default_factory=list, init=False)
    def get_rounds(self) -> List[Round]:
        return self.rounds
    votes: list[Vote] = field(default_factory=list, init=False)