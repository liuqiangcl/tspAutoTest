#-*- coding:utf-8 -*-
'''
Created on 2016-12-26
@author: Hunk
'''
import time
import unittest
from cases.testCinemasCase import cinemasCase
from cases.testScreensCase import screensCase
from cases.testQueryOrderCase import queryOrdeCase
from cases.testFilmsCase import filmsCase
from cases.testSessiondaysCase import sessiondaysCase
from cases.testSessionsCase import sessionsCase
from cases.testSessionseatCase import sessionseatCase
from cases.testCancelOrderCase import cancelOrdeCase
from cases.testCreateOrderCase import createOrdeCase
from cases.testCreateCancelOrderCase import CreateCancelCase
from cases.testCreateConfirmlOrderCase import CreateConfirmlOrderCase  #创建->确认
from cases.testCreateConfirmlRefundOrderCase import CreateConfirmlRefundOrderCase  #创建->确认->退单
from comm import HTMLTestRunner

  # 将用例组装数组
# testcases = [cinemasCase,screensCase,filmsCase,sessionsCase,sessiondaysCase,sessionseatCase,queryOrdeCase,CreateConfirmlOrderCase,CreateCancelCase,CreateConfirmlRefundOrderCase]
# testcases =[CreateCancelCase]
testcases = [CreateConfirmlOrderCase]
# testcases = []
def Test_Report():
    testunit=unittest.TestSuite()#构建测试套间
    #循环读取数组中的用例
    for case in testcases:
      testunit.addTest(unittest.makeSuite(case))
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) #获取当前时间
    reportname = 'report/'+'Result_'+current_time+'.html'#定义报告路径
    fp = open(reportname, 'wb')#测试报告模板
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试报告', description=u'用例执行情况：')
    return runner.run(testunit)
    
if __name__ == '__main__':
    Test_Report()