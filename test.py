import os

# 定义文件夹路径
folder_path = "/Users/areay7/Desktop/rgb"

# 获取文件名列表并按ascll码排序
file_list = sorted(os.listdir(folder_path))

# 输出排序后的文件名列表
print(file_list)