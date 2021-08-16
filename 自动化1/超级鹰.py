# -*- coding:utf-8 -*-
# import requests
# from hashlib import md5
#
# class Chaojiying_Client(object):
#
#     def __init__(self, username, password, soft_id):
#         self.username = username
#         password =  password.encode('utf8')
#         self.password = md5(password).hexdigest()
#         self.soft_id = soft_id
#         self.base_params = {
#             'user': self.username,
#             'pass2': self.password,
#             'softid': self.soft_id,
#         }
#         self.headers = {
#             'Connection': 'Keep-Alive',
#             'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
#         }
#
#     def PostPic(self, im, codetype):
#         """
#         im: 图片字节
#         codetype: 题目类型 参考 http://www.chaojiying.com/price.html
#         """
#         params = {
#             'codetype': codetype,
#         }
#         params.update(self.base_params)
#         files = {'userfile': ('ccc.jpg', im)}
#         r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
#         return r.json()
#
#     def ReportError(self, im_id):
#         """
#         im_id:报错题目的图片ID
#         """
#         params = {
#             'id': im_id,
#         }
#         params.update(self.base_params)
#         r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
#         return r.json()
#
#
# # chaojiying = Chaojiying_Client('xuzhuzhu', '123456', '917858')	#用户中心>>软件ID 生成一个替换 96001
# # im = open('code.jpg', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
# # print(chaojiying.PostPic(im, 9004)['pic_str'])	# #1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
#
# from selenium import webdriver
# from time import sleep
# from PIL import Image
# from selenium.webdriver import ActionChains
# drv=webdriver.Chrome(executable_path='./chromedriver.exe')
# drv.get('https://kyfw.12306.cn/otn/resources/login.html')
# script = 'Object.defineProperty(navigator,"webdriver",{get:()=>undefined,});'
# drv.execute_script(script)
# sleep(1)
# a=drv.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a')
# drv.maximize_window()
# a.click()
# sleep(1)
#
#
# drv.save_screenshot('c.png')
# code=drv.find_element_by_xpath('//*[@id="J-loginImg"]')
# location=code.location
# size=code.size
# rang=(int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height']))
# i=Image.open('./c.png')
# codename = './code.png'
# fname=i.crop(rang)
# fname.save(codename)
#
# # img=drv.find_element_by_xpath(
# #     '//*[@id="J-loginImg"]').screenshot('./code.png')  #直接定位验证码图片标签位置截图
# chaojiying = Chaojiying_Client('xuzhuzhu', '123456', '917858')	#用户中心>>软件ID 生成一个替换 96001
# im = open('code.png', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
# result=(chaojiying.PostPic(im, 9004)['pic_str'])
#
# all_list = []
# if '|' in result:
#     list_item = result.split('|')
#     count = len(list_item)
#     for i in range(count):
#         x_y = []
#         x = int(list_item[i].split(',')[0])
#         y = int(list_item[i].split(',')[1])
#         x_y.append(x)
#         x_y.append(y)
#         all_list.append(x_y)
# else:
#     x_y = []
#     x = int(result.split(',')[0])
#     y = int(result.split(',')[1])
#     x_y.append(x)
#     x_y.append(y)
#     all_list.append(x_y)
# print(all_list)
#
# for l in all_list:
#     x = l[0]
#     y = l[1]
#     ActionChains(drv).move_to_element_with_offset(code ,x, y).click().perform()
#     sleep(0.5)
# drv.find_element_by_xpath('//*[@id="J-userName"]').send_keys('18806673502')
# drv.find_element_by_xpath('//*[@id="J-password"]').send_keys('xu200305')
# drv.find_element_by_xpath('//*[@id="J-login"]').click()
# sleep(3)
#
# span = drv.find_element_by_xpath('//*[@id="nc_1_n1z"]')
# action = ActionChains(drv)
# action.click_and_hold(span)
# action.move_by_offset(350, 0).perform()
# action.release()
#
# sleep(5)
#
# drv.quit()
