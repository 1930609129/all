# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options
# from browsermobproxy import Server
# from time import sleep
#
# server = Server("H:\\browsermob-proxy-2.1.4-bin\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat")
# server.start()
# proxy = server.create_proxy()
# proxy.new_har("generated_har")
# proxy.blacklist(".*google.*", 404)
# proxy.blacklist(".*yahoo.*", 404)
# proxy.blacklist(".*facebook.*", 404)
# proxy.blacklist(".*twitter.*", 404)
# # proxy = server.create_proxy({"httpProxy":"61.155.141.13:20345"})
# chrome_options = Options()
# chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))
# chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
# #针对UA请求头的操作，防止因为没有添加请求头导致的访问被栏截了
# chrome_options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) >AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
# #实现规避操作
# web=Chrome(options=chrome_options,executable_path='A:\学习资料\chat\自动化2\chromedriver.exe')
# web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
#   "source": """
#     Object.defineProperty(navigator, 'webdriver', {
#       get: () => undefined
#     })
#   """
# })
#
# proxy.new_har("ht_list2", options={ 'captureContent': True})
# web.get('https://weibo.com/tv/home')
# sleep(10)
# result = proxy.har
# # lst=[]
# # def img_lst():
# #   div_lst=web.find_elements_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[3]//div[@class="u-col-3"]/div[@class="woo-box-item-inlineBlock"]')
# #   for div in div_lst:
# #     # web.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# #     img=div.find_element_by_xpath('./div/div/div[1]/img').get_attribute('src')
# #     lst.append(img)
# #
# # def img():
# #   web.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# #   img_lst()
# # img()
#
# print(result)





# from selenium import webdriver
# import time
#
# from browsermobproxy import Server
#
# server = Server("H:\\browsermob-proxy-2.1.4-bin\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat")
# server.start()
# proxy = server.create_proxy()
# proxy.new_har("generated_har")
# proxy.blacklist(".*google.*", 404)
# proxy.blacklist(".*yahoo.*", 404)
# proxy.blacklist(".*facebook.*", 404)
# proxy.blacklist(".*twitter.*", 404)
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--proxy-server={0}".format(proxy.proxy))
# print(proxy.proxy)
# browser = webdriver.Chrome(executable_path="A:\学习资料\chat\自动化2\chromedriver.exe")
# proxy.new_har("//weibo.com/tv/home",options={'captureHeaders': True, 'captureContent': True})
# url = 'https://weibo.com/tv/home'
# browser.get(url)
# time.sleep(8)
# result = proxy.har
#
# print(result['log']['entries'])
# server.stop()
# browser.quit()
# proxy.close()

# from browsermobproxy import Server
# from selenium import webdriver
# import time
# import pprint
#
# class ProxyManger:
#
#     __BMP = "H:\\browsermob-proxy-2.1.4-bin\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat"
#
#     def __init__(self):
#
#         self.__server = Server(ProxyManger.__BMP)
#         self.__client = None
#
#     def start_server(self):
#         self.__server.start()
#         return self.__server
#
#     def start_client(self):
#
#         self.__client = self.__server.create_proxy(params={"trustAllServers": "true"})
#         return self.__client
#
#     @property
#     def client(self):
#         return self.__client
#
#     @property
#     def server(self):
#         return self.__server
#
# if __name__=="__main__":
#     # 开启Proxy
#     proxy = ProxyManger()
#     server = proxy.start_server()
#     client = proxy.start_client()
#
#     # 配置Proxy启动WebDriver
#     options = webdriver.ChromeOptions()
#     options.add_argument("--proxy-server={}".format(client.proxy))
#     options.add_argument('--ignore-certificate-errors')
#     driver = webdriver.Chrome(executable_path='A:\学习资料\chat\自动化2\chromedriver.exe', chrome_options=options)
#
#     # 获取返回的内容
#     client.new_har("home")
#     driver.get("https://weibo.com/tv/")
#     time.sleep(12)
#
#     newHar = client.har
#     pprint.pprint(newHar['log']['entries'])
#     server.stop()


import requests
#####   视频下载

# url='https://weibo.com/tv/api/component?'
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43",
#     'Referer':'https://weibo.com/tv/show/1034:4654260705755180?mid=4654260912396601',
#     'cookie':'SUB=_2AkMXgQHkf8NxqwJRmfoXxGjhaYp2zwvEieKh3fA_JRMxHRl-yT9jql4ctRB6PAEvC7wHVcKDYmjm1mJJOSZ4ZYuNIQw-;'
# }
# data={
#     'data': '{"Component_Play_Playinfo":{"oid":"1034:4654260705755180"}}'
# }
# con=requests.post(url,headers=headers,data=data).json()
# g=f"http:{con['data']['Component_Play_Playinfo']['urls']['高清 720P']}"
# mp4=requests.get(url=g,headers=headers,data=data).content
# with open('a.mp4','wb') as m:
#     m.write(mp4)

import time
#### 提取链接相关信息
url='https://weibo.com/tv/api/component?'
def html():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43",
        'Referer':'https://weibo.com/tv/home',
        'cookie':'SUB=_2AkMXgQHkf8NxqwJRmfoXxGjhaYp2zwvEieKh3fA_JRMxHRl-yT9jql4ctRB6PAEvC7wHVcKDYmjm1mJJOSZ4ZYuNIQw-; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhxZMUFTTX5ZXe3rJg8KEOQ; SINAGLOBAL=1337983642994.6667.1625132752340; UOR=,,ntp.msn.cn; login_sid_t=726524ec1459bb1f3d58c4984a0bdf35; cross_origin_proto=SSL; _s_tentry=ntp.msn.cn; Apache=7024010049814.078.1625232003512; ULV=1625232003523:9:9:9:7024010049814.078.1625232003512:1625216955354; TC-V-WEIBO-G0=b09171a17b2b5a470c42e2f713edace0; XSRF-TOKEN=HcbOeNocq6ubbmXFHRAHu6ff'
    }
    data={
        'data': '{"Component_Home_Recommend":{}}'
    }
    con=requests.post(url,headers=headers,data=data).json()
    lst=con['data']['Component_Home_Recommend']['list']
    for dic in lst:
        mp4_lst(dic['mid'],dic['oid'])
def mp4_lst(mid,oid):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43",
        'Referer':f'https://weibo.com/tv/show/1034:4654260705755180?mid={mid}',
        'cookie':'SUB=_2AkMXgQHkf8NxqwJRmfoXxGjhaYp2zwvEieKh3fA_JRMxHRl-yT9jql4ctRB6PAEvC7wHVcKDYmjm1mJJOSZ4ZYuNIQw-; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhxZMUFTTX5ZXe3rJg8KEOQ; SINAGLOBAL=1337983642994.6667.1625132752340; UOR=,,ntp.msn.cn; login_sid_t=726524ec1459bb1f3d58c4984a0bdf35; cross_origin_proto=SSL; _s_tentry=ntp.msn.cn; Apache=7024010049814.078.1625232003512; ULV=1625232003523:9:9:9:7024010049814.078.1625232003512:1625216955354; TC-V-WEIBO-G0=b09171a17b2b5a470c42e2f713edace0; XSRF-TOKEN=HcbOeNocq6ubbmXFHRAHu6ff'
    }
    a='{"Component_Play_Playinfo":{"oid":"'f'{oid}''"}}'
    data={
        'data': a
    }
    con=requests.post(url,headers=headers,data=data).json()
    g=f"http:{con['data']['Component_Play_Playinfo']['urls']['高清 720P']}"
    mp4=requests.get(url=g,headers=headers,data=data).content
    lj=f'./web/{mid}.mp4'
    with open(lj,'wb') as m:
        m.write(mp4)
    time.sleep(3)
html()