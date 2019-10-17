# coding=UTF-8
import time
import unittest
import HTMLTestRunner
import logging
from app import path1, log
from case.case_hrm1 import HRM_employee_01
from BeautifulReport import BeautifulReport

log()

suit = unittest.TestSuite()
suit.addTest(unittest.makeSuite(HRM_employee_01))
#
# BeautifulReport(suit).report(filename='/rep.html',log_path= path1+'/report',
#                              description='v10')

with open(path1+'/report/rep.html','wb') as f:
    runner =HTMLTestRunner.HTMLTestRunner(f,title='text', description='老子的报告')
    runner.run(suit)
