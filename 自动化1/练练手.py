# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
drv=webdriver.Chrome(executable_path='./chromedriver.exe')
# drv.get('https://passport.jd.com/new/login.aspx')
# a=drv.find_element_by_xpath("//div[@class='login-tab login-tab-r']/a")
# a.click()
# drv.maximize_window()
# name=drv.find_element_by_id('loginname')
# pwd=drv.find_element_by_id('nloginpwd')
# name.send_keys('123')
# pwd.send_keys('321')
# b=drv.find_element_by_xpath('//*[@id="loginsubmit"]')
# b.click()
# c=drv.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]')
# action=ActionChains(drv)
# action.click_and_hold(c)
# for i in range(3):
#     action.move_by_offset(10,0).perform()
#     sleep(0.3)
# action.release()
# sleep(3)
# drv.quit()
