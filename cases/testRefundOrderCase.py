#-*- coding:utf-8 -*-
'''
Created on 2016-01-03
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
class refundOrdeCase(unittest.TestCase):
  ##初始化工作 
  def setUp(self):
  	pass
    #具体的测试用例，一定要以test开头 
  def testrefundOrde(self): 
    u'''退单'''
    refundOrderUrl = "trade/refundorder"
    refundOrderParam = {'orderId':'20170106231710817389551696740352','callbackUrl':'callbackUrl'}
    RESTFulClient = RESTFulClientPost.RESTFulClientPost(refundOrderUrl,refundOrderParam)
    print(RESTFulClient.RESTFulClientPost()[0])
    # self.assertTrue (RESTFulClient.RESTFulClientPost()[0] == 200 )
    # print (createOrderParam)
  # #退出清理工作 
  def tearDown(self): 
    pass
if __name__ =='__main__':
	unittest.main()