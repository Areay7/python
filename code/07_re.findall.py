import re

# 1.findall方法,返回匹配的结果列表
rs = re.findall('\d+','chuan13zhi24')
print(rs)

# 2.findall方法中,flag参数的作用
rs = re.findall('a.bc','a\nbc')
rs = re.findall('a.bc','a\nbc',re.DOTALL)
rs = re.findall('a.bc','a\nbc',re.S)
print(rs)  # ['a\nbc']

# 3. findall方法中分组的使用
rs = re.findall('a.+bc','a\nbc',re.DOTALL)
print(rs)  # ['a\nbc']

rs = re.findall('a(.)+bc','a\nbc',re.DOTALL)
print(rs)   # ['\n']
