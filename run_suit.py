import time
import unittest
import logging
from app import path1, log
from case.case_hrm1 import HRM_employee_01
from BeautifulReport import BeautifulReport

log()
try:
    suit = unittest.TestSuite()
    suit.addTest(unittest.makeSuite(HRM_employee_01))


    BeautifulReport(suit).report(filename='/{}.html'.format(time.strftime('%H%M%S'),log_path= path1+'/report'),
                                 description='报告')

except Exception as e :
    print('错误走这里')
    print(e)
    logging.info(e)