# 1.导入模块
import requests

# 2.发送请求,获取响应
responese = requests.get('http://www.baidu.com')

# print(responese)

# 3.获取响应数据
# print(responese.encoding)
responese.encoding='utf-8'
# print(responese.text)

print(responese.content.decode())
