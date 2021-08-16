# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions
from time import sleep
chrome_options = Options()
chrome_options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
# chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
drv=webdriver.Chrome(executable_path='./chromedriver.exe',options=chrome_options)
drv.get('https://kyfw.12306.cn/otn/resources/login.html')
a=drv.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a')
drv.maximize_window()
a.click()
sleep(3)
drv.quit()





















# from lxml import etree
# from time import sleep
# from selenium import webdriver
# import requests
# from selenium.webdriver import ActionChains
# from hashlib import md5
# #封装超级鹰打码识别函数
# #executable_path输入谷歌驱动的位置
# bro = webdriver.Chrome(executable_path='./chromedriver.exe')
# #浏览器全屏
# bro.maximize_window()
# #12306登陆首页
# bro.get('https://kyfw.12306.cn/otn/resources/login.html')
# sleep(1)
# #选择"账号登陆"并点击
# a_tag = bro.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a')
# a_tag.click()
# #定位账号和密码的位置，并在'xxx'部分输入对应的账号和密码
# bro.find_element_by_id('J-userName').send_keys('xxx')
# sleep(2)
# bro.find_element_by_id('J-password').send_keys('xxx')
# sleep(2)