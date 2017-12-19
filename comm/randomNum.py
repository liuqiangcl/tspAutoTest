#-*- coding:utf-8 -*-
import datetime;  
import random;  
def getRandomNum():
	nowTime=datetime.datetime.now().strftime("%Y%m%d%H%M%S");#生成当前时间  
	randomNum=random.randint(0,100);#生成的随机整数n，其中0<=n<=100  
	if randomNum<=10:
		randomNum=str(0)+str(randomNum);  
	uniqueNum=str(nowTime)+str(randomNum);  
	return uniqueNum
if __name__ == '__main__':
	print (getRandomNum())  