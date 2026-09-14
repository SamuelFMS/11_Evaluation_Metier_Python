from models.round import Round
from models.vote import Vote


class goncourt:
    year: int
    rounds: list[Round]
    votes: list[Vote]