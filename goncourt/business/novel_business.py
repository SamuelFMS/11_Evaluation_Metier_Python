from business.business import Business
from dao.main_character_dao import MainCharacterDao
from dao.novel_dao import NovelDao
from dao.person_dao import PersonDao

class NovelBusiness(Business):
    novel_dao: NovelDao = NovelDao()
    person_dao: PersonDao = PersonDao()
    main_character_dao: MainCharacterDao = MainCharacterDao()

    def get_all(self):
        list_novels = self.novel_dao.get_all(self.connection.cursor())
        for novel in list_novels:
            if novel.id_novel:
                novel.author = self.person_dao.get_by_related_id(self.connection.cursor(), self.novel_dao, novel.id_novel)
                novel.main_character = self.main_character_dao.get_all_by_related_id(self.connection.cursor(), self.novel_dao, novel.id_novel)
        return list_novels