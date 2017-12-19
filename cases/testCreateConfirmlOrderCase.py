#-*- coding:utf-8 -*-
'''
Created on 2017-01-03
@author: Hunk
'''
import sys
sys.path.append("..")
import unittest
from comm import randomNum
from modes import RESTFulClientPost
from process import testResourceData as testData
from process import testOrderData
from process.buildData import buildData
testData = testData.getDataDict()
merchantOrderId =randomNum.getRandomNum()
class CreateConfirmlOrderCase(unittest.TestCase):
  ##初始化工作 
  def setUp(self):
  	pass
    #具体的测试用例，一定要以test开头 
  def testCreateOrder(self):
    u'''创建订单'''
    createOrderUrl = "trade/createorder"
    createOrderParam ={"cinemaCode":testData['cinemaCode'],"sessionId":testData["sessionId"],"mobile":"3J3fem93tBfyX2Y78XcGvQ==","merchantOrderId":merchantOrderId,"seat":testData['seatCode']}
    print(createOrderParam)
    RESTFulClient = RESTFulClientPost.RESTFulClientPost(createOrderUrl,createOrderParam)
    self.assertTrue(RESTFulClient.RESTFulClientPost()[0] == 200)
    return RESTFulClient.RESTFulClientPost()[1]
  def testConfirmOrder(self):
    u'''确认订单'''
    confirmOrderUrl = 'trade/confirmorder'
    confirmOrderParam = testOrderData.getConfirmOrderParam(self.testCreateOrder())
    # print(confirmOrderParam)
    RESTFulClient = RESTFulClientPost.RESTFulClientPost(confirmOrderUrl,confirmOrderParam)
    self.assertTrue(RESTFulClient.RESTFulClientPost()[0] == 200)
    # return RESTFulClient.RESTFulClientPost()[0]

  def tearDown(self):
      # #退出清理工作 
    pass
if __name__ =='__main__':
  # CreateConfirmlOrderCase = CreateConfirmlOrderCase()
  # print(CreateConfirmlOrderCase.testCreateOrder())
	unittest.main()
