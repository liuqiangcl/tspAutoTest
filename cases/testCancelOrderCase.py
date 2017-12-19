#-*- coding:utf-8 -*-
'''
Created on 2016-12-28
@author: Hunk
'''
'''取消订单'''
import sys
sys.path.append("..")
import unittest
from modes import RESTFulClientPost
class cancelOrdeCase(unittest.TestCase):
  ##初始化工作 
  def setUp(self):
  	pass
    #具体的测试用例，一定要以test开头 
  def testCancelOrder(self): 
    u'''取消订单'''
    cancelOrderUrl = "trade/cancelorder"
    orderParam = {"orderId":"20170109161326818370078801133568"}
    RESTFulClient = RESTFulClientPost.RESTFulClientPost(cancelOrderUrl,orderParam)
    self.assertTrue(RESTFulClient.RESTFulClientPost()[0] == 200)
    # print (RESTFulClient.RESTFulClientPost()[1])
  # #退出清理工作 
  def tearDown(self): 
    pass
if __name__ =='__main__':
	unittest.main()