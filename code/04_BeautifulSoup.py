# 1.导入模块
from bs4 import BeautifulSoup

# 2.准备文档字符串
html = '''  <html>
                <head>
                    <title>aaa</title>
                    <a id='link'> bbb </a>
                </head>  
'''

# 3.创建BeatutifulSoup对象
soup = BeautifulSoup(html,'html.parser')

# 4.创建title标签
title = soup.find('title')
print(title)


# 5.查找所有 a 标签
a_s = soup.find_all('a')
print(a_s)

# 二.根据属性进行查找
# 查找id为link的标签
# 方式1：通过命名参数进行指定
a = soup.find(id ='link')
print(a)

# 方式2： 使用attrs来指定属性字典,进行查找
a = soup.find(attrs={'id' : 'link'})
print(a)

# 三. 根据文本内容查找
text = soup.find(text='aaa')
print(text)

# Tag对象
print(type(a)) # <class 'bs4.element.Tag'>
print('标签名',a.name)
print('标签名所以属性',a.attrs)
print('标签名文本内容',a.text)




