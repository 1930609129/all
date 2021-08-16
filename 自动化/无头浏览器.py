# -*- coding:utf-8 -*-
# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium import webdriver
foptions = webdriver.FirefoxOptions()
foptions.add_argument('-headless')
browser = webdriver.Firefox(options=foptions)
drv=webdriver.Firefox(executable_path='./geckodriver.exe',options=foptions)
drv.get('https://www.baidu.com/')
print(drv.page_source)
drv.quit()
