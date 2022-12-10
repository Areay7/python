# 导入正则模块
import re

# 字段匹配
rs = re.findall("abc",'dsadsadsaabcdasdsa')
rs = re.findall('a.c','adcabvsaadcdsasac')
rs = re.findall('a.c','a\nc')  # .不能匹配换行符  能匹配其余任意
rs = re.findall('a[BC]c','aBc')
print(rs)   # ['aBc']

# 预定义的字符集
rs = re.findall('\d','123')
rs = re.findall('\w' , 'Axdsa44654_中文$%^#')
print(rs)  # ['A', 'x', 'd', 's', 'a', '4', '4', '6', '5', '4', '_', '中', '文']

# 数量词
rs = re.findall('a\d*','a123')
rs = re.findall('a\d+','aaa1')
rs = re.findall('a\d?','aaa1')
rs = re.findall('a\d{2}','a2131')
print(rs)   # ['a21']

