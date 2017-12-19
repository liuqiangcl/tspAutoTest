#-*- coding:utf-8 -*-
import  hashlib
def GetStrMd5(src):
    m=hashlib.md5()
    m.update(bytes(src,encoding = "utf8"))
    return m.hexdigest()


if __name__ == '__main__':
	# md5 = GetStrMd5('1_1')
	md5 = GetStrMd5("cinemacode=78654908,merchantorderid=201612280001,mobile=3J3fem93tBfyX2Y78XcGvQ==,seat=['78654908%2301%2317'],sessionid=23706")
	md51 = GetStrMd5("cinemacode=78654908,merchantorderid=201612280001,mobile=3J3fem93tBfyX2Y78XcGvQ==,seat=['78654908%2301%2317'],sessionid=23706")
	print (md51)
	print (md5)