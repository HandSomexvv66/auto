import unittest
import requests
from api.api1 import api_hrm
from app import TOkne


class HRM_employee_02(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.session = requests.session()
        cls.api = api_hrm()

        reponse = cls.api.logon_api(cls.session, '13800000002', '123456')
        cls.token = reponse.json().get('data')


        reponse1 = cls.api.add_api1(cls.session, cls.token)
        print(reponse1.json())

        cls.id1 = reponse1.json().get('data').get('id')


    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    def test_1_select(self):

        response = self.api.select_api(self.session,self.id1, self.token)
        print(response.json())

    def test_02_undate(self):
        response = self.api.update_api(self.session,self.id1,self.token)
        print(response.json())

    def test_03_delete(self):
        reponse = self.api.delete_api(self.session,self.id1,self.token)
        print(reponse.json().get('success'))

