# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
drv=webdriver.Firefox(executable_path='./geckodriver.exe')
drv.get('https://www.taobao.com/')
setinput=drv.find_element_by_id('q')
setinput.send_keys('苹果')
btn=drv.find_element_by_css_selector('.btn-search')
drv.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(1)
btn.click()
drv.get('http://www.baidu.com/')
sleep(2)
drv.back()
sleep(2)
drv.forward()
sleep(3)
drv.quit()