from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
#针对UA请求头的操作，防止因为没有添加请求头导致的访问被栏截了
chrome_options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) >AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
#实现规避操作
web=Chrome(options=chrome_options)
web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
# web.get('https://www.lagou.com/')
# web.find_element_by_xpath('//*[@id="cboxClose"]').click()
# sleep(1)
# web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python',Keys.ENTER)
# lst=web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li')
# for li in lst:
#     h=li.find_element_by_tag_name('h3').text
#     hh=li.find_element_by_xpath('./div/div/div[2]/div/span').text
#     print(h)
#     print(hh)

web.get('https://www.12306.cn/index/index.html')
sleep(1)
web.find_element_by_xpath('//*[@id="fromStationText"]').click()
sleep(0.1)
web.find_element_by_xpath('//*[@id="fromStationText"]').send_keys('广州',Keys.ENTER)
sleep(1)
web.find_element_by_xpath('//*[@id="toStationText"]').send_keys('深圳',Keys.ENTER)
sleep(1)
web.find_element_by_xpath('//*[@id="isHighDan"]').click()
sleep(1)
web.find_element_by_xpath('//*[@id="search_one"]').click()
sleep(1)
# frame=web.find_elements_by_tag_name('iframe')
# sleep(2)
# web.find_element_by_xpath('//*[@id="gb_closeDefaultWarningWindowDialog_id"]').click()
# sleep(2)
web.quit()