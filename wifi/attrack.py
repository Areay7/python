from tkinter import *
from tkinter import ttk
import psutil
import time
import tkinter.filedialog  # 在Gui中打开文件浏览
import tkinter.messagebox  # 打开tkiner的消息提醒框
import pywifi  # Add this import statement


class MY_GUI:
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

        self.get_value = StringVar()
        self.get_wifi_value = StringVar()
        self.get_wifimm_value = StringVar()

        self.wifi = pywifi.PyWiFi()
        self.iface = None  # 先将iface设置为None

        # 尝试获取第一个无线网卡，如果获取失败，则设置iface为None
        try:
            self.iface = self.get_first_interface()
            # 断开连接并像以前一样断言状态
        except (IndexError, AttributeError, AssertionError) as e:
            print(f"Error: Unable to initialize wifi interface. {e}")
            self.iface = None

    def __str__(self):
        if self.iface:
            return f'(INTERFACE: {self.iface.name})'
        else:
            return '(INTERFACE: None)'

    def get_first_interface(self):
        # 获取所有网络接口
        interfaces = psutil.net_if_stats().keys()
        # 选择第一个有线接口（ethernet）
        for iface in interfaces:
            if "eth" in iface.lower() or "en" in iface.lower():
                return iface
        return None

    # 设置窗口
    def set_init_window(self):
        self.init_window_name.title("WIFI破解工具")
        self.init_window_name.geometry('+500+200')

        labelframe = LabelFrame(width=400, height=200, text="配置")  # 框架，以下对象都是对于labelframe中添加的
        labelframe.grid(column=0, row=0, padx=10, pady=10)

        self.search = Button(labelframe, text="搜索附近WiFi", command=self.scans_wifi_list).grid(column=0, row=0)

        self.pojie = Button(labelframe, text="开始破解", command=self.readPassWord).grid(column=1, row=0)

        self.label = Label(labelframe, text="目录路径：").grid(column=0, row=1)

        self.path = Entry(labelframe, width=12, textvariable=self.get_value).grid(column=1, row=1)

        self.file = Button(labelframe, text="添加密码文件目录", command=self.add_mm_file).grid(column=2, row=1)

