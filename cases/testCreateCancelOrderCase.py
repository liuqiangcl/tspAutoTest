#-*- coding:utf-8 -*-
'''
Created on 2017-01-03
@author: Hunk
'''
'''创建订单'''
import sys
sys.path.append("..")
import unittest
from comm import randomNum
from modes import RESTFulClientPost
from process import testResourceData as testData
from process.buildData import buildData
testData = testData.getDataDict()
merchantOrderId =randomNum.getRandomNum()
class CreateCancelCase(unittest.TestCase):
  ##初始化工作 
  def setUp(self):
  	pass
    #具体的测试用例，一定要以test开头 
  def testCreateOrder(self):
    u'''创建订单'''
    createOrderUrl = "trade/createorder"
    createOrderParam ={"cinemaCode":testData['cinemaCode'],"sessionId":testData["sessionId"],"mobile":"3J3fem93tBfyX2Y78XcGvQ==","merchantOrderId":merchantOrderId,"seat":testData['seatCode']}
    RESTFulClient = RESTFulClientPost.RESTFulClientPost(createOrderUrl,createOrderParam)
    self.assertTrue(RESTFulClient.RESTFulClientPost()[0] == 200)
    return RESTFulClient.RESTFulClientPost()[1]
  def getOrderId(self):
    '''获取订单号'''
    OrderData = buildData(self.testCreateOrder())
    return OrderData.testOrderData("orderId")
  def testCancelOrder(self): 
    u'''取消订单'''
    cancelOrderUrl = "trade/cancelorder"
    orderParam = {"orderId":"%s" % (self.getOrderId())}
    RESTFulClient = RESTFulClientPost.RESTFulClientPost(cancelOrderUrl,orderParam)
    self.assertTrue(RESTFulClient.RESTFulClientPost()[0] == 200)
    return RESTFulClient.RESTFulClientPost()[1]

  def tearDown(self):
      # #退出清理工作 
    pass
if __name__ =='__main__':
  # OrderCase = createOrdeCase()
  # print (OrderCase.testCreateOrder())
  # print (OrderCase.getOrderId())
  # print (OrderCase.testCancelOrder())
	unittest.main()
