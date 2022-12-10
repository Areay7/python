import json
# 1. 把PYTHON转换为JSON字符串
# 1.1 PYTHON类型的数据
json_str = '''[{"currentConfirmedIncr":0,"confirmedIncr":0,"curedIncr":0,"deadIncr":0,"showRank":true,
"yesterdayConfirmedCount":2147383647,"yesterdayLocalConfirmedCount":2147383647,"yesterdayOtherConfirmedCount":2147383647,
"yesterdayAsymptomaticCount":2147383647,"highDanger":"","midDanger":"","highInDesc":"","lowInDesc":"","outDesc":""}]'''
rs = json.loads(json_str)  # 转为python数据


# 1.2 把PYTHON类型的数据转换为JSON字符串
json_str = json.dumps(rs,ensure_ascii=False)
print(json_str)


# 2. 把PYTHON以JSON格式存储到文件
# 2.1 构建要写入文件对象
with open('../data/test01.json','w') as fp:
    # 2.2 把PYTHON以JSON格式存储到文件中
    json.dump(rs,fp,ensure_ascii=False)