from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
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
web.get("https://www.lagou.com/")
web.find_element_by_xpath('//*[@id="cboxClose"]').click()
sleep(1)
web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python',Keys.ENTER)
lis=web.find_elements_by_class_name('position_link')
n=1
for i in lis:
    i.find_element_by_tag_name('h3').click()
    web.switch_to_window(web.window_handles[-1])
    text=web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]').text
    f=open('a/%d'%n,'w',encoding='utf-8')
    f.write(text)
    f.close()
    web.close()
    web.switch_to_window(web.window_handles[0])
    sleep(3)
    n+=1