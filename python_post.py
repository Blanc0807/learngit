# -*- coding:utf8 -*-

import urllib
import urllib2

url = ""

#headers	
headers = {}

data = {}
data[""] = ""
#数据编码
data = urllib.urlencode(data)
#请求
req = urllib2.Request(url, data, headers)
#打开地址，并赋值给变量
ResponseStr = urllib2.urlopen(req)
ResponseStr = ResponseStr.read()
#转码打印
ResponseStr = ResponseStr.decode("unicode_escape")
print(ResponseStr)