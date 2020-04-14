#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/4/14 上午 10:26 
# @File : run.py 
# @Software: PyCharm
# @Author : LiTian

import subprocess
import ctypes


# 模拟按下降低音量按键
def set_speaker_vol(num):
    WM_APPCOMMAND = 0x319
    APPCOMMAND_VOLUME_UP = 0x0a
    APPCOMMAND_VOLUME_DOWN = 0x09
    APPCOMMAND_VOLUME_MUTE = 0x08

    hwnd = ctypes.windll.user32.GetForegroundWindow()
    ctypes.windll.winmm.waveOutSetVolume(hwnd, 0xffffffff)

    for i in range(num):
        ctypes.windll.user32.PostMessageA(hwnd, WM_APPCOMMAND, 0, APPCOMMAND_VOLUME_DOWN * 0x10000)


# 使用window命令netsh wlan show network，获取搜索到的wifi列表
def get_wifi_list():
    result = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
    result = result.decode('gbk')
    lst = result.split('\r\n')

    # 处理列表文本获取wifi名队列
    wifi_name = []
    for s in lst:
        if 'SSID' in s:
            wifi_name.append(s.split(':')[1].strip())
    return wifi_name


if __name__ == '__main__':
    wifi_name = get_wifi_list()
    if 'Midea' in wifi_name:
        print('Midea')
        set_speaker_vol(50)
