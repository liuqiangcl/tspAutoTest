#-*- coding:utf-8 -*-
'''
Created on 2016-12-26
@author: Hunk
'''
'''创建订单'''
import sys
import json
import logging
sys.path.append("..")
# from comm import log
from comm import randomNum
from modes import RESTFulClientPost
from process import testResourceData as testData
from process.buildData import buildData
from process import testOrderData
testData = testData.getDataDict()
merchantOrderId =randomNum.getRandomNum()
def CreateOrder():
	createOrderUrl = "trade/createorder"
	createOrderParam ={"cinemaCode":testData['cinemaCode'],"sessionId":testData["sessionId"],"mobile":"3J3fem93tBfyX2Y78XcGvQ==","merchantOrderId":merchantOrderId,"seat":testData['seatCode']}
	# print (createOrderParam)
	RESTFulClient = RESTFulClientPost.RESTFulClientPost(createOrderUrl,createOrderParam)
	# print (RESTFulClient.RESTFulClientPost()[1])
	return RESTFulClient.RESTFulClientPost()[1]


def getOrderId():
	'''获取订单号'''
	OrderData = buildData(CreateOrder())
	return OrderData.testOrderData("orderId")

# def CancelOrder(): 
#     u'''取消订单'''
#     cancelOrderUrl = "trade/cancelorder"
#     orderParam = {"orderId":"%s" % (getOrderId())}
#     RESTFulClient = RESTFulClientPost.RESTFulClientPost(cancelOrderUrl,orderParam)
#     print (RESTFulClient.RESTFulClientPost()[1])
def ConfirmOrder():
	# print(CreateOrder())
	confirmOrderUrl = 'trade/confirmorder'
	confirmOrderParam = testOrderData.getConfirmOrderParam(CreateOrder())
	RESTFulClient = RESTFulClientPost.RESTFulClientPost(confirmOrderUrl,confirmOrderParam)
	return RESTFulClient.RESTFulClientPost()[0]
if __name__ == '__main__':
	# pass
	print(CreateOrder())
	# print(ConfirmOrder())
	# for i in range(0,350):
	# 	ConfirmOrder()
	# 	print (i)
	# 