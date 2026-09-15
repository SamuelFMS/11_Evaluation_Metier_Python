from dataclasses import dataclass, field
from typing import Optional


@dataclass
class MainCharacter:
    id_main_character: Optional[int] = field(default=None, init=False)
    name: str