import json
import unittest
import requests
from parameterized import parameterized
from api.api1 import api_hrm
from app import path1


def date_login():
    list1 = []
    with open(path1 + '/date/login_date.json', 'r', encoding='utf-8') as f:
        date = json.load(f)

        for i in date:
            for b in i.values():
                list1.append((b.get('mobile'), b.get('password'), b.get('message'), b.get('code'), b.get('success')))
    return list1


class HRM_login(unittest.TestCase):

    def setUp(self):
        self.session = requests.session()
        self.api = api_hrm()

    def tearDown(self):
        self.session.close()

    @parameterized.expand(date_login())
    def test_01_login(self, mobile, password, message, code, success):
        reponse = self.api.logon_api(self.session, mobile, password)
        self.assertEqual(message, reponse.json().get('message'))
        self.assertEqual(code, reponse.json().get('code'))
        self.assertEqual(success, reponse.json().get('success'))



    def test_02_add(self):
        reponse = self.api.logon_api(self.session,'13800000002','123456')
        self.token = reponse.json().get('data')
        print(self.token)

        reponse1 = self.api.add_api1(self.session,self.token)
        print(reponse1.json())


