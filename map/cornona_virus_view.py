"""
全国疫情可视化地图开发
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取数据
f = open("../data/last_day_cornoa_virus_of_china.json", encoding='utf-8')
data = f.read()  # 获取全部数据
# 关闭资源
f.close()
# 读取各省数据
# 将json字符串转换为python字典
data_dict = json.loads(data)   # 基础字典数据
#  从字典中取出个省份
#  组装每个省份和确诊人数为元组 ， 并将各个省份都封装到列表内
data_list = []  #   绘图所使用都数据表
for province_data in data_dict:
    province_name = province_data["provinceShortName"]   # 省份名
    province_data = province_data["currentConfirmedCount"]  # 确认人数
    data_list.append((province_name, province_data))

# 构建地图对象
map = Map()
# 添加数据
map.add("各省份确诊人数", data_list, "china")
# 设置全局选项
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,   # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[
            {"min":1, "max": 99, "lable": "1~99人", "color": "#CCFFFF"},
            {"min": 100, "max": 909, "lable": "10~909人", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "lable": "1000~4999人", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "lable": "5000~9999人", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "lable": "10000~99999人", "color": "#CC3333"},
            {"min": 100000,  "lable": "100000+", "color": "#990033"},
        ]
    )
)
# 绘图
map.render("全国疫情地图.html")



