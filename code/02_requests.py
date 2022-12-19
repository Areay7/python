# 1.导入模块
import requests

# 2.发送请求,获取响应
responese = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia')


# 3.从响应中,获取响应数据
print(responese.content.decode())