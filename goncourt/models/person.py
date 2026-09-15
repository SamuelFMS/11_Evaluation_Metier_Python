from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Person:
    id_person: Optional[int] = field(default=None, init=False)
    firstname: str
    lastname: str
    biography: str