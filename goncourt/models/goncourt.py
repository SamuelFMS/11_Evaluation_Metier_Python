from dataclasses import dataclass

from models.round import Round
from models.vote import Vote

@dataclass
class Goncourt:
    year: int
    rounds: list[Round]
    votes: list[Vote]