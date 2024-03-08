import gdb
import matplotlib.pyplot as plt

# 启用 GDB 的 Python API
gdb.execute("python import sys")
gdb.execute("python sys.path.append('/path/to/your/python/scripts')")

# GDB Python 扩展中的函数，用于获取变量的值
def get_variable_value(var_name):
    try:
        value = gdb.parse_and_eval(var_name)
        return value
    except gdb.error as e:
        return None

# 变量名列表
variable_names = ['var1', 'var2', 'var3']

# 提取变量的值
variable_values = {}
for var_name in variable_names:
    value = get_variable_value(var_name)
    if value is not None:
        variable_values[var_name] = value

# 可视化变量
plt.bar(variable_values.keys(), [float(value) for value in variable_values.values()])
plt.xlabel('Variables')
plt.ylabel('Values')
plt.title('Variable Visualization')
plt.show()
