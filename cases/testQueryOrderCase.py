#-*- coding:utf-8 -*-
'''
Created on 2016-12-26
@author: Hunk
'''
'''查询订单信息'''
import sys
sys.path.append("..")
import unittest
from modes import RESTFulClientPost
class queryOrdeCase(unittest.TestCase):
  ##初始化工作 
  def setUp(self):
  	pass
    #具体的测试用例，一定要以test开头 
  def testQueryOrder(self): 
    u'''查询订单信息'''
    queryOrderUrl = "trade/queryorder"
    orderParam = {"orderId":"20161221110533811407228601896960"}
    RESTFulClient = RESTFulClientPost.RESTFulClientPost(queryOrderUrl,orderParam)
    self.assertTrue(RESTFulClient.RESTFulClientPost()[0] == 200)
  # #退出清理工作 
  def tearDown(self): 
    pass
if __name__ =='__main__':
	unittest.main()