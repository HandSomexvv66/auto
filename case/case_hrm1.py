# coding=UTF-8
import unittest
import requests
from api.api1 import api_hrm


class HRM_employee_01(unittest.TestCase):
    id1 = ''
    token = ''

    @classmethod
    def setUpClass(cls):
        cls.session = requests.session()
        cls.api = api_hrm()

    @classmethod
    def tearDownClass(cls):
        cls.session.close()

    def test_1_add(self):
        reponse = self.api.logon_api(self.session, '13800000002', '123456')
        HRM_employee_01.token = reponse.json().get('data')

        reponse1 = self.api.add_api1(self.session, HRM_employee_01.token)
        print(reponse1.json())

        HRM_employee_01.id1 = reponse1.json().get('data').get('id')
        # con = pymysql.Connect(host='182.92.81.159', user='readuser', password='iHRM_user_2019', database='ihrm',
        #                       autocommit=True)
        # consor = con.cursor()
        # consor.execute("select * from bs_user where username = '勒布朗科比'")
        # date3 = consor.fetchall()
        # print('数据库:', date3)

    def test_2_select(self):
        response = self.api.select_api(self.session, HRM_employee_01.id1, HRM_employee_01.token)
        print(response.json())

    def test_3_undate(self):
        response = self.api.update_api(self.session, HRM_employee_01.id1, HRM_employee_01.token)
        print(response.json())
        # con = pymysql.Connect(host='182.92.81.159',user='readuser',password='iHRM_user_2019',database='ihrm',autocommit=True)
        # consor = con.cursor()
        # consor.execute("select * from bs_user where id = {}".format(HRM_employee_01.id1))
        # date3=consor.fetchall()
        # print(date3)

    def test_4_delete(self):
        reponse = self.api.delete_api(self.session, HRM_employee_01.id1, HRM_employee_01.token)
        print(reponse.json())
