#-*- coding:utf-8 -*-
'''
Created on 2016-12-26
@author: Hunk
'''
'''查询场次座位信息'''
import sys
sys.path.append("..")
import unittest
from process import testResourceData as testData
from modes import RESTFulClientGet
testData = testData.getDataDict()
class sessionseatCase(unittest.TestCase):
  ##初始化工作 
  def setUp(self):
  	pass
    #具体的测试用例，一定要以test开头 
  def testSessionseat(self): 
    u'''查询场次座位信息'''
    sessionseatUrl = "info/sessionseat?cinemaCode=%s&sessionId=%s" % (testData["cinemaCode"],testData["sessionId"])
    self.assertTrue(RESTFulClientGet.RESTFulClientGet(sessionseatUrl)[0] == 200)
    print(RESTFulClientGet.RESTFulClientGet(sessionseatUrl)[1])
  # #退出清理工作 
  def tearDown(self): 
    pass
if __name__ =='__main__':
	unittest.main()