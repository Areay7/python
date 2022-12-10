import re
# 1. 在不使用r原串的时候,遇到转义符怎么做

rs = re.findall('a\nbc','a\nbc')
print(rs)  # ['a\nbc']

rs = re.findall('a\\\\nbc','a\\nbc')
print(rs)  # ['a\\nbc']

# r原串在正则中就可以消除转义符带来的影响
rs = re.findall(r'a\\\nbc','a\\\nbc')
print(rs)  # ['a\\\nbc']

# 扩展: 可以解决写正则的时候，不符合PEP8规范的问题
rs = re.findall(r'\d','a123')
print(rs)  # ['1', '2', '3']