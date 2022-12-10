# 1.导入相关模块
import re

import requests
from bs4 import BeautifulSoup

# 2.发送请求,获取疫情首页内容
response = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')
home_page = response.content.decode()
# print(home_page)

# 3.使用BeautifulSoup提取疫情数据
soup = BeautifulSoup(home_page,'html.parser')
script = soup.find(id='getListByCountryTypeService2true')
text = script.text
# print(text)

# 4.使用正则表达式,提取json字符串
json_str = re.findall(r'\[.+\]', text)[0]
print(json_str)