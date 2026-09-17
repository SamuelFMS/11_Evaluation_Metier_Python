from typing import Optional

from business.business import Business
from dao.main_character_dao import MainCharacterDao
from dao.novel_dao import NovelDao
from dao.person_dao import PersonDao
from dao.round_dao import RoundDao
from dao.vote_dao import VoteDao
from models.novel import Novel


class NovelBusiness(Business):
    novel_dao: NovelDao = NovelDao()
    person_dao: PersonDao = PersonDao()
    main_character_dao: MainCharacterDao = MainCharacterDao()
    round_dao: RoundDao = RoundDao()
    vote_dao: VoteDao = VoteDao()

    def get_by_id(self, id: int) -> Optional[Novel]:
        """
        Retrieves a novel by its ID.
        :param id:
        :return:
        """
        novel = self.novel_dao.get_by_id(self.get_connection().cursor(), id)
        if novel is not None and novel.id_novel is not None:
            novel.author = self.person_dao.get_by_related_id(self.get_connection().cursor(), self.novel_dao,
                                                             novel.id_novel)
            novel.main_character = self.main_character_dao.get_all_by_related_id(self.get_connection().cursor(),
                                                                                 self.novel_dao, novel.id_novel)
        return novel

    def get_all(self) -> list[Novel]:
        """
        Retrieves all novels from the database.
        :return:
        """
        list_novels = self.novel_dao.get_all(self.get_connection().cursor())
        if list_novels:
            for novel in list_novels:
                if novel.id_novel:
                    novel.author = self.person_dao.get_by_related_id(self.get_connection().cursor(), self.novel_dao,
                                                                     novel.id_novel)
                    novel.main_character = self.main_character_dao.get_all_by_related_id(self.get_connection().cursor(),
                                                                                         self.novel_dao, novel.id_novel)
        return list_novels

    def get_all_from_round(self, round_id: int) -> list[Novel]:
        """
        Retrieves all the novel that gave the given round.
        :param round_id: id of the round
        :return:
        """
        list_novels = self.novel_dao.get_all_by_tiers_table_related_id(self.get_connection().cursor(), self.round_dao,
                                                                       "step", round_id)
        if list_novels:
            for novel in list_novels:
                if novel.id_novel:
                    novel.author = self.person_dao.get_by_related_id(self.get_connection().cursor(), self.novel_dao,
                                                                     novel.id_novel)
                    novel.main_character = self.main_character_dao.get_all_by_related_id(self.get_connection().cursor(),
                                                                                         self.novel_dao, novel.id_novel)
        return list_novels

    def add_novel_to_round(self, novel_id: int, id_round: int, year: int) -> bool:
        """
        Add a novel to a round
        :param novel_id: id of the novel
        :param id_round: id of the round
        :param year:
        :return:
        """
        connection = self.get_connection()
        cursor = connection.cursor()
        round_number = self.round_dao.get_number(cursor, id_round)
        round_number_max = self.round_dao.get_max_round_number(cursor, year)
        if round_number == round_number_max:
            self.vote_dao.add_vote_for_year(cursor, novel_id, year)

        if self.novel_dao.add_novel_to_round(cursor, novel_id, id_round):
            connection.commit()
            return True
        else:
            connection.rollback()
            raise RuntimeError("Une erreur c'est produite lors de l'ajout du roman au round")

    def remove_novel_from_round(self, novel_id: int, id_round: int, year: int) -> bool:
        """
        Remove a novel from a round
        :param novel_id: id of the novel
        :param id_round: id of the round
        :param year:
        :return:
        """
        connection = self.get_connection()
        cursor = connection.cursor()
        if self.novel_dao.remove_novel_to_round(cursor, novel_id, id_round):
            if self.vote_dao.remove_vote_for_year(cursor, novel_id, year):
                connection.commit()
                return True
            else:
                connection.rollback()
                raise RuntimeError("Une erreur c'est produite lors de le la suppression du roman au vote")
        else:
            connection.rollback()
            raise RuntimeError("Une erreur c'est produite lors de l'ajout du roman au round")
