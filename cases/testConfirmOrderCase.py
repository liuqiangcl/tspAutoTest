#-*- coding:utf-8 -*-
'''
Created on 2017-01-03
@author: Hunk
'''
'''确认订单'''
import sys
sys.path.append("..")
import unittest
from process import testResourceData as testData
from modes import RESTFulClientPost
testData = testData.getDataDict()
class confirmOrderCase(unittest.TestCase):
  ##初始化工作 
  def setUp(self):
  	pass
    #具体的测试用例，一定要以test开头 
  def testconfirmOrder(self):

    u'''确认订单'''
    confirmOrderUrl = 'trade/confirmorder'
    confirmOrderParam = {'seatDetail': "[{'seatCode':'78654908%2319%2311','priceId':120,'ticketMoney':8888,'serviceFee':300}]", 'callbackUrl': 'callbackUrl', 'orderId': '20170105170638816933918677663744'}
    RESTFulClient = RESTFulClientPost.RESTFulClientPost(confirmOrderUrl,confirmOrderParam)
    self.assertTrue(RESTFulClient.RESTFulClientPost()[0] == 200)
  # #退出清理工作 
  def tearDown(self): 
    pass
if __name__ =='__main__':
	unittest.main()