
#-*- coding:utf-8 -*-
#sha256 加密
import sys
sys.path.append("..")
import hashlib,hmac
import base64

# /* 生成签名Authorization */

def hmacb64(accountId,macKey,macData ):
    secret  = bytes(macKey, 'utf-8')  
    message = bytes(macData, 'utf-8')
    # accountId = accountId.decode()
    signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest()).decode()
    return 'hmac username="%s",algorithm="hmac-sha256", headers="X-Date Content-Md5", signature="%s"' %(accountId,signature)




if __name__ == '__main__':
    accountId ='1_1'
    macData = "DADIBL"
    macKey = "123456"
    print (hmacb64(macKey,macData,accountId))