from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from models.main_character import MainCharacter
from models.person import Person


@dataclass
class Novel:
    title: str
    summary: str
    editor: str
    publication_date: date
    number_of_pages: int
    ISBN: int
    publisher_price: Decimal
    author: Person
    main_character: MainCharacter