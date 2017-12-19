#-*- coding:utf-8 -*-
'''
Created on 2016-12-26
@author: Hunk
'''
import sys
sys.path.append("..")
import requests
from comm.systemAuth import SystemAuth
from comm import md5
class RESTFulClientPost(SystemAuth):
	def __init__(self,url,param):
		SystemAuth.__init__(self,url)
		self.param = param
	# def printParam(self):
	# 	print(self.accountId)
	def getParamMd5(self):
		paramList = []
		for key,value in self.param.items():
			paramList.append((key.lower()+'='+value))
		sortParam=",".join(sorted(paramList))
		# print(sortParam)
		return md5.GetStrMd5(sortParam)

	def getHeader(self):
		return {"Content-Type":"application/x-www-form-urlencoded",
           "Content-Md5":self.getParamMd5(),
           "X-Date":self.getTime(),
           "Authorization":self.getAuth()
           }
	def RESTFulClientPost(self):
		r1 = requests.post(self.url,data = self.param,headers = self.getHeader())
		return r1.status_code,r1.text
		# return 
if __name__ == '__main__':
	confirmOrderUrl = 'trade/confirmorder'
	confirmOrderParam = {"orderId":"20170103174207816218072024088576","seatDetail":"[{'seatCode':'78654908%2308%2307','priceId':120,'ticketMoney':8888,'serviceFee':300}]","callbackUrl":"callbackUrl"}
	RESTFulClientPost = RESTFulClientPost(confirmOrderUrl,confirmOrderParam)
	print (RESTFulClientPost.getParamMd5())