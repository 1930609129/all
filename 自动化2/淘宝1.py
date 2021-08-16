from selenium import webdriver
from time import sleep
import csv
import re
from threading import Thread,Lock
bankLock = Lock()
def tao(key):
    web.find_element_by_id('q').send_keys(key)
    web.find_element_by_class_name('btn-search').click()
    sleep(20)
    page = web.find_element_by_xpath('//*[@id="mainsrp-pager"]/div/div/div/div[1]').text
    page = re.findall("(\d+)", page)
    return page
def get_content():
    web.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    web.implicitly_wait(1)
    divs=web.find_elements_by_xpath('//div[@class="items"]/div[@class="item J_MouserOnverReq  "]')
    for div in divs:
        text=div.find_element_by_xpath('.//div[@class="row row-2 title"]/a').text
        jpg = div.find_element_by_xpath('.//div[@class="pic"]/a/img').get_attribute('src')
        newjpg=None
        if jpg.endswith('jpg') or jpg.endswith('webp'):
            newjpg=jpg
        price=div.find_element_by_xpath('.//strong').text+"元"
        deal=div.find_element_by_xpath('.//div[@class="deal-cnt"]').text
        name = div.find_element_by_xpath('.//div[@class="shop"]/a').text
        # print(text,price,deal,name,newjpg,sep='|')
        with open('data2.csv','a',newline="",encoding='utf-8') as f:
            csvfile=csv.writer(f,delimiter=',')
            csvfile.writerow([text,newjpg,price,deal,name])



def main():
    page=tao(keyword)
    get_content()
    page = int(page[0])
    page_num = 1
    thead_list = []
    while page_num < page:
        t=Thread(target=main1,args=(page_num,))
        t.start()
        thead_list.append(t)
        page_num+=1
    for t in thead_list:
        t.join()

def main1(page_num):
    bankLock.acquire()
    print(f"正在爬取{page_num + 1}页的数据")
    web.get(f'https://s.taobao.com/search?q={keyword}&s={page_num * 44}')
    web.implicitly_wait(2)
    get_content()
    bankLock.release()

if __name__ == '__main__':
    keyword = input('输入商品关键字')
    web = webdriver.Chrome()
    web.get('https://www.taobao.com/')
    main()

""" 
"""