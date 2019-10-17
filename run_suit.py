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
    BeautifulReport(suit).report(filename='/rep.html',log_path= path1+'/report',
                                 description='v10')

except Exception as e :
    print(e)
    logging.info(e)