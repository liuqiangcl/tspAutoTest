#-*- coding:utf-8 -*-
import sys
sys.path.append("..")
from comm import hmacb64
from comm import md5
import time
import requests
class SystemAuth(object):
	"""docstring for ClassName"""
	def __init__(self,url,accountId = '1_1',macKey = '123456'):
		self.url = "http://123.57.68.222:8000/"
		self.accountId = accountId
		self.macKey = macKey
		self.url = self.url + url
	def getParamMd5(self):
		if '?' in self.url :
			Parameter = self.url.split('?')[-1]
			return (md5.GetStrMd5(','.join(sorted(Parameter.replace("&",",").lower().strip("").split(',')))))
		else:
			return (md5.GetStrMd5(self.accountId))
	def getTime(self):
		return time.strftime(u"%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
	#/*获取格林尼治时间*/
	def getxData(self):
			return "X-Date: " + self.getTime()
	# /* md5值加上前缀 */
	def getContentMd5(self):
		contentMd5 = "Content-Md5: " + self.getParamMd5()
		return contentMd5

	#生成需要加密的串
	def getMacData(self):
		return self.getxData() + "\n" + self.getContentMd5()

	#/*计算签名*/
	def getAuth(self):
		authorization = hmacb64.hmacb64(self.accountId,self.macKey,self.getMacData())
		return authorization

	def getHeader(self):
		return {"Content-Type":"application/json",
           "Content-Md5":self.getParamMd5(),
           "X-Date":self.getTime(),
           "Authorization":self.getAuth()
           }
	def getParam(self):
		print (self.url)


if __name__ == '__main__':
	url = "info/cinemas"
	auth = SystemAuth(url)
	print(auth)
	headers = auth.getHeader()
	r = requests.get(auth.url,headers=headers)
	print(r.status_code)
