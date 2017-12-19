#-*- coding:utf-8 -*-
'''
Created on 2016-12-26
@author: Hunk
'''
'''创建订单'''
import sys
sys.path.append("..")
import unittest
from comm import randomNum
from modes import RESTFulClientPost
from process import testResourceData as testData
testData = testData.getDataDict()
merchantOrderId =randomNum.getRandomNum()
class createOrdeCase(unittest.TestCase):
  ##初始化工作 
  def setUp(self):
  	pass
    #具体的测试用例，一定要以test开头 
  def testCreateOrder(self): 
    u'''创建订单'''
    createOrderUrl = "trade/createorder"
    # createOrderParam ={"cinemaCode":testData['cinemaCode'],"sessionId":testData["sessionId"],"mobile":"tDTFduWnXjCbcXVYGDuYjg==","merchantOrderId":merchantOrderId,"seat":testData['seatCode']}
    createOrderParam = {'cinemaCode': '78654908', 'sessionId': '23798', 'seat': "['78654908%2319%2311']", 'mobile': '3J3fem93tBfyX2Y78XcGvQ==', 'merchantOrderId': '2017010517574929'}
    RESTFulClient = RESTFulClientPost.RESTFulClientPost(createOrderUrl,createOrderParam)
    self.assertTrue(RESTFulClient.RESTFulClientPost()[0] == 200)
    # return RESTFulClient.RESTFulClientPost()[1]
    # print (createOrderParam)
  # #退出清理工作 
  def tearDown(self): 
    pass
if __name__ =='__main__':
	unittest.main()