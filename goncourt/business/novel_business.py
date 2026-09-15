from business.business import Business
from dao.main_character_dao import MainCharacterDao
from dao.novel_dao import NovelDao
from dao.person_dao import PersonDao
from dao.round_dao import RoundDao
from models.novel import Novel


class NovelBusiness(Business):
    novel_dao: NovelDao = NovelDao()
    person_dao: PersonDao = PersonDao()
    main_character_dao: MainCharacterDao = MainCharacterDao()
    round_dao: RoundDao = RoundDao()

    def get_all(self)-> list[Novel]:
        list_novels = self.novel_dao.get_all(self.connection.cursor())
        if list_novels:
            for novel in list_novels:
                if novel.id_novel:
                    novel.author = self.person_dao.get_by_related_id(self.connection.cursor(), self.novel_dao, novel.id_novel)
                    novel.main_character = self.main_character_dao.get_all_by_related_id(self.connection.cursor(), self.novel_dao, novel.id_novel)
        return list_novels

    def get_all_from_round(self, round_id:int) -> list[Novel]:
        list_novels = self.novel_dao.get_all_by_tiers_table_related_id(self.connection.cursor(),self.round_dao,"step", round_id)
        if list_novels:
            for novel in list_novels:
                if novel.id_novel:
                    novel.author = self.person_dao.get_by_related_id(self.connection.cursor(), self.novel_dao, novel.id_novel)
                    novel.main_character = self.main_character_dao.get_all_by_related_id(self.connection.cursor(), self.novel_dao, novel.id_novel)
        return list_novels