from datetime import date

from models.novel import Novel


class Round:
    number: int
    date_round: date
    ketps_novel: list[Novel]