#-*- coding:utf-8 -*-
'''
Created on 2016-12-26
@author: Hunk
'''
'''查询影城营业日期'''
import sys
sys.path.append("..")
import unittest
from modes import RESTFulClientGet
from process import testResourceData as testData
testData = testData.getDataDict()
class sessiondaysCase(unittest.TestCase):
  ##初始化工作 
  def setUp(self):
  	pass
    #具体的测试用例，一定要以test开头 
  def testSessiondays(self): 
    u'''查询影城营业日期'''
    sessionseatUrl = "info/sessiondays?cinemaCode=%s" % (testData["cinemaCode"])
    self.assertTrue(RESTFulClientGet.RESTFulClientGet(sessionseatUrl)[0] == 200)
  # #退出清理工作 
  def tearDown(self): 
    pass
if __name__ =='__main__':
	unittest.main()