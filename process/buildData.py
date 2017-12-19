#-*- coding:utf-8 -*-
'''
Created on 2016-12-27
@author: Hunk
'''
import sys
import re
import time
import json
import logging
import requests
sys.path.append("..")
# from comm import log
from modes.RESTFulClientGet import RESTFulClientGet
# from comm import systemAuth

class buildData(object):
	"""docstring for buildData"""
	def __init__(self,jsonData,key1="data"):
		self.jsonData = jsonData
		self.key1 = key1
		# self.key2 = key2
		# self.key3 = key3
	def testData(self,key2,key3):
		u'''构建查询数据'''
		dataSet = []
		json_dict = json.loads(self.jsonData)
		for keyValue in json_dict.get(self.key1).get(key2): 
			dataSet.append(keyValue.get(key3))
		return dataSet
	def testOrderData(self,key2):
		u'''构建订单ID'''
		json_dict = json.loads(self.jsonData)
		json_dict.get(self.key1).get(key2)
		try:
			return json_dict.get(self.key1).get(key2)
		except Exception as e:
			logging.error(e)

if __name__ == '__main__':
	'''查询影厅信息'''
	cinemasParam = "info/cinemas"
	cinemas = RESTFulClientGet(cinemasParam)
	cinema = cinemas[1]
	print(cinema)