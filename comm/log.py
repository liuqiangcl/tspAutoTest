import logging
logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)
# 建立一个filehandler来把日志记录在文件里，级别为debug以上
fh = logging.FileHandler("logs/data.log")
# fh.setLevel(logging.DEBUG)
# 建立一个streamhandler来把日志打在CMD窗口上，级别为error以上
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# 设置日志格式
formatter = logging.Formatter("%(asctime)s - %(module)s - %(lineno)d - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
fh.setFormatter(formatter)
#将相应的handler添加在logger对象中
logger.addHandler(ch)
logger.addHandler(fh)
# 开始打日志

# random.randint(0,len(sessionDaysData[0]))