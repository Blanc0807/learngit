# -*- coding:utf8 -*-
import urllib
import urllib2 
url = 'http://exmple'
#定义请求数据，并对数据进行赋值
data = {}
data["key"] = "value"
#对请求数据进行编码
data = urllib.urlencode(data)
#讲数据和url进行连接
request = url + '?' + data
#向服务器发送请求
requestResponse = urllib2.uropen(request)
#读取服务端返回数据，转换
ResponseStr = requestResponse.read()
#打印结果
ResponseStr = ResponseStr.decode("unicode_escape")
print(requestResponse)