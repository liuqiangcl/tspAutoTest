'''
Created on 2017-01-04
@author: Hunk
'''
import sys
import urllib.parse
import json
def getConfirmOrderParam(CreateOrderInfo):
    CreateOrderInfo = json.loads(CreateOrderInfo)
    data = CreateOrderInfo.get("data")
    orderId = data.get("orderId")
    orderSnapshot = data.get("ticketOrder").get("orderSnapshot")
    orderSnapshotList = list(eval(orderSnapshot))
    for i in orderSnapshotList:
        for j in i.get("price"):
            if j.get("ticketType") == '1':
                ticketMoney = j.get("salePrice")
                priceId = j.get("priceId")
        seatCode = urllib.parse.quote(i.get("seatCode"))
    confirmOrderParam = {"orderId":orderId,"seatDetail":"[{'seatCode':'%s','priceId':%s,'ticketMoney':%s,'serviceFee':300}]" % (seatCode,priceId,ticketMoney),"callbackUrl":"callbackUrl"}
    return confirmOrderParam