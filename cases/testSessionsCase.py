#-*- coding:utf-8 -*-
'''
Created on 2016-12-26
@author: Hunk
'''
'''查询场次信息'''
import sys
sys.path.append("..")
import unittest
from process import testResourceData as testData
testData = testData.getDataDict()
from modes import RESTFulClientGet
class sessionsCase(unittest.TestCase):
  ##初始化工作 
  def setUp(self):
  	pass
    #具体的测试用例，一定要以test开头 
  def testSessions(self): 
    u'''查询场次信息'''
    # sessionsUrl = "info/sessions?cinemaCode=%s&showDate=%s" % (testData["cinemaCode"],testData["showDate"])
    sessionsUrl = "info/sessions?cinemaCode=%s&showDate=%s" % ("78654908","2017-02-17")
    # print (RESTFulClientGet.RESTFulClientGet(sessionsUrl)[1])
    # self.assertTrue(RESTFulClientGet.RESTFulClientGet(sessionsUrl)[0] == 200)
    print (RESTFulClientGet.RESTFulClientGet(sessionsUrl)[1])
    # return(RESTFulClientGet.RESTFulClientGet(sessionsUrl)[1])
  # #退出清理工作 
  def tearDown(self): 
    pass
if __name__ =='__main__':
  # SC = sessionsCase()
  # print(SC.testSessions())
	unittest.main()