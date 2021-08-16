# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
drv=webdriver.Firefox(executable_path='./geckodriver.exe')
drv.get('https://qzone.qq.com/')
drv.switch_to_frame('login_frame')
a=drv.find_element_by_id('switcher_plogin')
a.click()
name=drv.find_element_by_id('u')
pwd=drv.find_element_by_id('p')
name.send_keys('1930609129')
pwd.send_keys('12345678')
sleep(2)
btn=drv.find_element_by_id('login_button')
btn.click()
sleep(3)
drv.quit()