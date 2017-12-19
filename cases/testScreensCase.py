#-*- coding:utf-8 -*-
'''
Created on 2016-12-26
@author: Hunk
'''
'''查询影厅信息'''
import sys
sys.path.append("..")
import unittest
from modes import RESTFulClientGet
from process import testResourceData as testData
testData = testData.getDataDict()
class screensCase(unittest.TestCase): 
  ##初始化工作 
  def setUp(self): 
    pass
    #具体的测试用例，一定要以test开头 
  def testScreens(self):
    u'''查询影厅信息'''
    screensUrl = "info/screens?cinemaCode=%s" %(testData["cinemaCode"])
    # screensUrl = "info/screens?cinemaCode=%s" %("78654908")
    self.assertTrue(RESTFulClientGet.RESTFulClientGet(screensUrl )[0] == 200)
    # print(RESTFulClientGet.RESTFulClientGet(screensUrl )[1])
  #退出清理工作 
  def tearDown(self): 
    pass
if __name__ =='__main__':
	unittest.main()