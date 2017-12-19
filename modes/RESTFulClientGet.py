#-*- coding:utf-8 -*-
'''
Created on 2016-12-26
@author: Hunk
'''
import sys
sys.path.append("..")
import requests
from comm import systemAuth

def RESTFulClientGet(url):
	auth = systemAuth.SystemAuth(url)
	headers = auth.getHeader()
	r1 = requests.get(auth.url,headers=headers)
	return r1.status_code,r1.text
	# return r1.text
if __name__ == '__main__':
	'''查询影厅信息'''
	# screensParam = "info/sessionseat?cinemaCode=78654908&sessionId=23706"
	# Param = "info/cinemas"
	sessionsUrl = "info/sessions?cinemaCode=%s&showDate=%s" % ("78654908","2017-11-11")
	print(RESTFulClientGet(sessionsUrl))