#!/usr/bin/python3
#-*-coding:utf-8 -*-
'''
 40-49：背景色
 40: 黑 41: 红 42: 绿 43: 黄  44: 蓝 45: 紫 46: 绿 47: 白
 30-39：字体颜色
 30: 黑 31: 红 32: 绿 33: 黄  34: 蓝 35: 紫 36: 绿 37: 白
'''
c = r'''
none         = "\033[0m"
black        = "\033[0;30m"
dark_gray    = "\033[1;30m"
blue         = "\033[0;34m"
light_blue   = "\033[1;34m"
green        = "\033[0;32m"
light_green -= "\033[1;32m"
cyan         = "\033[0;36m"
light_cyan   = "\033[1;36m"
red          = "\033[0;31m"
light_red    = "\033[1;31m"
purple       = "\033[0;35m"
light_purple = "\033[1;35m"
brown        = "\033[0;33m"
yellow       = "\033[1;33m"
light_gray   = "\033[0;37m"
white        = "\033[1;37m"

'''
# print(c)
colors = {
    'none': "\033[0m",
    'black': "\033[0;30m",
    'dark_gray': "\033[1;30m",
    'blue': "\033[0;34m",
    'dark_blue': "\033[1;34m",
    'green': "\033[0;32m",
    'dark_green': "\033[1;32m",
    'light_green': "\033[2;32m",
    'cyan': "\033[0;36m",
    'dark_cyan': "\033[1;36m",
    'red': "\033[0;31m",
    'dark_red': "\033[1;31m",
    'purple': "\033[0;35m",
    'dark_purple': "\033[1;35m",
    'brown': "\033[0;33m",
    'yellow': "\033[1;33m",
    'dark_gray': "\033[0;37m",
    'white': "\033[1;37m",
}

print('\033[41;32;5m 闪光\033[0m') #闪光字符，在windows里面没有测试出效果，在pycharm里面没有效果，在linux里面测试出效果
print('\007响一声！\033[0m') #发出声音 在windows里面测试出效果，在pycharm里面没有效果，在linux里面测试出效果
print('\033[43;34;4m 下划线\033[0m')
print('\033[45;36;7m 反显\033[0m')
print('\033[47;31;8m 消隐\033[0m') #看不到了

for i, item in enumerate(colors):
    print(i, '%s%s- a quick brown fox jump over the lazy dog%s' % (item, colors[item], colors['none']))
