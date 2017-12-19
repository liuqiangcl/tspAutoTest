#-*- coding:utf-8 -*-
'''
Created on 2016-12-26
@author: Hunk
'''
'''查询影片信息'''
import sys
sys.path.append("..")
import unittest
from modes import RESTFulClientGet
from process import testResourceData as testData
testData = testData.getDataDict()
class filmsCase(unittest.TestCase):
  ##初始化工作 
  def setUp(self):
  	pass
    #具体的测试用例，一定要以test开头 
  def testfilms(self):
    u'''查询影片信息'''
    filmsUrl = "info/films?cinemaCode=%s" % (testData["cinemaCode"])
    self.assertTrue(RESTFulClientGet.RESTFulClientGet(filmsUrl)[0] == 200)
  # #退出清理工作 
  def tearDown(self): 
    pass
if __name__ =='__main__':
	unittest.main()