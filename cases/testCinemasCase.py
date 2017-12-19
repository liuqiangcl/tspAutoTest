#-*- coding:utf-8 -*-
'''
Created on 2016-12-26
@author: Hunk
'''
'''查询影院列表'''
import sys
sys.path.append("..")
import unittest
from modes import RESTFulClientGet
class cinemasCase(unittest.TestCase):
  ##初始化工作 
  def setUp(self):
  	pass
    #具体的测试用例，一定要以test开头 
  def testCinemas(self):
    u'''查询影院列表''' 
    cinemasUrl = "info/cinemas"
    print (RESTFulClientGet.RESTFulClientGet(cinemasUrl)[1]) 
    self.assertTrue(RESTFulClientGet.RESTFulClientGet(cinemasUrl)[0] == 200)

  # #退出清理工作 
  def tearDown(self): 
    pass
if __name__ =='__main__':
	unittest.main()