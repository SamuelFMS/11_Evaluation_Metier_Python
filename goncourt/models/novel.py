from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal
from typing import Optional

from models.main_character import MainCharacter
from models.person import Person


@dataclass
class Novel:
    id_novel: Optional[int] = field(default=None, init=False)
    title: str
    summary: str
    editor: str
    publication_date: date
    number_of_pages: int
    ISBN: int
    publisher_price: Decimal
    author: Optional[Person] = field(default=None, init=False)
    main_character: list[MainCharacter] = field(default_factory=list, init=False)