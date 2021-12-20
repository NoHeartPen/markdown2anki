# 该模块用于启动Anki后, 在导入已处理的文件前, 通过按下Y键发起一次同步,

import pyautogui
import os 

os.system("D:\\03Program\\Anki\\anki.exe")

pyautogui.hotkey('y')

# pyautogui.hotkey('ctrl','shift','i') 很遗憾, 不支持模拟按下Ctrl+Shift+I打开文件夹