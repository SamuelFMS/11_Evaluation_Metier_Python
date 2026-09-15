from dataclasses import field, dataclass
from typing import Optional

from models.person import Person

@dataclass
class Jury:
    id_jury: Optional[int] = field(default=None, init=False)
    is_president: bool
    person: Person