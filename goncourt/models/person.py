from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Person:
    id_author: Optional[int] = field(default=None, init=False)
    first_name: str
    last_name: str
    biography: str