"""
pip install wxmsg -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pyautogui==0.9.53 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pyperclip==1.8.2 -i https://pypi.tuna.tsinghua.edu.cn/simple

"""

from wxmsg import WxMsg

i=0
while i<10:
    wx = WxMsg(speed=1)
    wx.send('666','Just do youself ~')
    i +=1