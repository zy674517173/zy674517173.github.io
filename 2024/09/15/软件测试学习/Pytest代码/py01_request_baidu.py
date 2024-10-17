# 导包
import requests

# 发送 http 请求，访问百度，得到相应结果
resp = requests.get(url = 'http://baidu.com')

print(resp.text)