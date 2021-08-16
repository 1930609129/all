# -*- coding:utf-8 -*-

from selenium import webdriver
from lxml import etree
from time import sleep
drv=webdriver.Firefox(executable_path='./geckodriver.exe')
drv.get('http://scxk.nmpa.gov.cn:81/xk/')
text=drv.page_source
tree=etree.HTML(text)
li_list=tree.xpath('//ul[@id="gzlist"]/li')
for li in li_list:
    name=li.xpath('./dl/@title')[0]
    print(name)
sleep(5)

drv.quit()
