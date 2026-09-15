from business.business import Business
from dao.goncourt_dao import GoncourtDao


class GoncourtBusiness(Business):
    goncourt_dao = GoncourtDao()
    def get_all(self):
        list_year = self.goncourt_dao.get_all(self.connection.cursor())
        return list_year