# -*- coding:utf-8 -*-
from selenium import webdriver
# 无头浏览器
from selenium.webdriver.chrome.options import Options
# 规避检测
from selenium.webdriver import ChromeOptions
import time
chrome_options = Options()
chrome_options.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
#针对UA请求头的操作，防止因为没有添加请求头导致的访问被栏截了
chrome_options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) >AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
#实现规避操作
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
browser = webdriver.Chrome(executable_path='./chromedriver.exe',options=chrome_options)
#browser = webdriver.Chrome()
script = '''
           Object.defineProperty(navigator, 'webdriver', {
               get: () => undefined
           })'''
browser.get('https://www.baidu.com/')
print(browser.page_source)
time.sleep(2)
browser.quit()