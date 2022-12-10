import json

# 1.把JSON字符串,转换为PYTHON数据
# 1.1 准备JSON字符串
json_str = '''[{"currentConfirmedIncr":0,"confirmedIncr":0,"curedIncr":0,"deadIncr":0,"showRank":true,
"yesterdayConfirmedCount":2147383647,"yesterdayLocalConfirmedCount":2147383647,"yesterdayOtherConfirmedCount":2147383647,
"yesterdayAsymptomaticCount":2147383647,"highDanger":"","midDanger":"","highInDesc":"","lowInDesc":"","outDesc":""}]'''

# 1.2 把JSON字符串.转换为PYTHON数据
rs = json.loads(json_str)
print(rs)
print(type(rs))  # <class 'list'>
print(type(rs[0]))  # <class 'dict'>


# 2.把JSON格式文件,转换为PYTHON类型数据
# 2.1 构建指向该文件的文件对象
with open('../data/test.json') as fp:
    # 2.2 加载该文件对象,转换为PYTHON类型的数据
    python_list = json.load(fp)
    print(python_list)
    print(type(python_list))
    print(type(python_list[0]))

