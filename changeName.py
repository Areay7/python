import os
import time

# 定义文件路径和起始数字
file_path = "/Users/areay7/Desktop/rgb"
start_num = 100

# 获取文件名列表
# file_list = os.listdir(file_path)


file_list = sorted(os.listdir(file_path))
file_list.sort(key=lambda x:int(x[:-4]))

print(file_list)

print("-------------------")


# 遍历文件名列表
for file_name in file_list:

    # 拼接原文件路径和新文件路径
    old_file_path = os.path.join(file_path, file_name)
    new_file_path = os.path.join(file_path, str(start_num) + '.png')

    # 重命名文件
    os.rename(old_file_path, new_file_path)

    print(str(start_num))
    # 更新起始数字
    start_num += 1



