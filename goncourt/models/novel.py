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

    def __str__(self) -> str:
        result = f"Titre : {self.title}\n"
        result += f"Auteur : {self.author.firstname} {self.author.lastname}\n" if self.author else "Auteur : Inconnu\n"
        result += f"Éditeur : {self.editor}\n"
        result += f"Date de publication : {self.publication_date.strftime('%d/%m/%Y')}\n"
        result += f"Nombre de pages : {self.number_of_pages}\n"
        result += f"ISBN : {self.ISBN}\n"
        result += f"Prix éditeur : {self.publisher_price:.2f} €\n"
        result += f"Résumé : {self.summary}\n"

        if self.main_character:
            result += "Personnages principaux :\n"
            for character in self.main_character:
                result += f"  - {character.name}\n"
        else:
            result += "Personnages principaux : Aucun\n"

        return result
