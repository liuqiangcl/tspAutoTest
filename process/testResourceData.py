#-*- coding:utf-8 -*-
'''
Created on 2016-12-28
@author: Hunk
'''
import sys
sys.path.append("..")
import time
import datetime
import urllib.parse
import logging
import random
# from comm import log
from process.buildData import buildData
from modes.RESTFulClientGet import RESTFulClientGet
#/*7.1.4	查询影片信息*/
filmsUrl = "info/films?cinemaCode=78654908"
# films = RESTFulClientGet(filmsUrl )

#/*7.1.2	查询影厅信息*/
screensUrl = "info/screens?cinemaCode=78654908"
# screens = RESTFulClientGet(screensUrl )


def getCinemaCode():
	'''查询影院列表'''
	cinemasUrl = "info/cinemas"
	cinemasData = RESTFulClientGet(cinemasUrl)[1]
	cinemasData = buildData(cinemasData)
	cinemasCode = cinemasData.testData('cinemas','cinemaCode')
	if len(cinemasCode) >= 2:
		cinemaCode = cinemasCode[1]
	else:
		cinemaCode = cinemasCode[0]
	return cinemaCode

def getShowDate(cinemaCode):
	'''查询影城营业日期'''
	sessionDaysUrl = "info/sessiondays?cinemaCode=%s" %(cinemaCode)
	sessionDays = RESTFulClientGet(sessionDaysUrl)[1]
	current_time = time.strftime("%Y-%m-%d",time.localtime(time.time()))

	# if current_time in sessionDays:
	# 	today = datetime.date.today()
	# 	showDate = today + datetime.timedelta(days=1)

	# 	# showDate = today + datetime.timedelta(days=1)
	# else:
	# 	sessionDaysData = buildData(sessionDays)
	# 	sessionDaysData = sessionDaysData.testData("cinemas","showDates")
	# 	showDate = sessionDaysData[0][random.randint(0,len(sessionDaysData[0])-1)]
	# return showDate
	return current_time

def getSessionId(cinemaCode,showDate):
	# 查询场次信息
	current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
	sessionsUrl = "info/sessions?cinemaCode=%s&showDate=%s" % (cinemaCode,showDate)
	sessionsData = RESTFulClientGet(sessionsUrl )[1]
	# print (sessionsData)  #获取场次信息报文
	sessionsData = buildData(sessionsData)
	showDate = sessionsData.testData('sessions','showDate')
	# print(showDate) #获取所有放映时间
	sessionsId = sessionsData.testData('sessions','sessionId')
	# print(sessionsId) #获取所有的场次IP
	try:
		#判断影片是否过期，获取一直查询未播放影片
		flag = True
		while flag:
			random_num = random.randint(0,len(sessionsId)-1)
			if int(current_time) < int(showDate[random_num]): #判断当前时间是否小于放映时间
				flag = False
			return sessionsId[random_num]
	except Exception as e:
		logging.error("无法获取场次")

def getSeatCode(cinemaCode,sessionId):
	'''查询场次座位信息'''
	sessionseatUrl = "info/sessionseat?cinemaCode=%s&sessionId=%s" % (cinemaCode,sessionId)
	sessionsSeatData = RESTFulClientGet(sessionseatUrl )[1]
	# print(sessionsSeatData)
	seatData = buildData(sessionsSeatData)
	# print(seatData)
	try:
		seatCode= seatData.testData('seats','seatCode')
		seatStatus= seatData.testData('seats','status')
		# print (seatStatus)
		i = 0
		while i <= (len(seatStatus)):
			if seatStatus[i] == "N":
				# print (seatStatus[i])
				return seatCode[i]
			else:
				i += 1
	except Exception as e:
		logging.error("无法获取场次座位图")
def getFilms(cinemaCode):
	'''查询影片信息'''
	filmsUrl = "info/films?cinemaCode=%s" %(cinemaCode)
	filmsData = RESTFulClientGet(filmsUrl)[1]
	filmsData = buildData(filmsData)
	films= filmsData.testData('films','filmName')
	return films

def parseSeatCode(seatCode):
	'''编码'''
	parseSeatCode = []
	try:
		parseSeatCode.append(urllib.parse.quote(seatCode)) 
	except Exception as e:
		logging.error("座位编码转换失败")
	else:
		return str(parseSeatCode)
	
	
def getDataDict():
	u'''构造数据字典'''
	cinemaCode = getCinemaCode()
	showDate = getShowDate(cinemaCode)		
	sessionId = getSessionId(cinemaCode,showDate)
	seatCode = getSeatCode(cinemaCode,sessionId)
	return {"cinemaCode":getCinemaCode(),"showDate":getShowDate(cinemaCode),
	"sessionId":getSessionId(cinemaCode,showDate),"seatCode":parseSeatCode(seatCode)}
	# return sessionId


if __name__ == '__main__':
	cinemaCode = getCinemaCode()
	print("影城Code:",cinemaCode)
	showDate = getShowDate(cinemaCode)
	print("营业日期:",showDate)
	sessionId = getSessionId(cinemaCode,"2017-03-23")
	print("场次ID:",sessionId)

	seatCode = getSeatCode(cinemaCode,sessionId)
	print("座位编码",seatCode)
	print("编码:",parseSeatCode(seatCode))
	films = getFilms(cinemaCode)
	print("上映的影片",films)