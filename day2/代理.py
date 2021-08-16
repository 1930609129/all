# -*- coding:utf-8 -*-

import requests
if __name__ == '__main__':
    url='https://www.baidu.com/s?wd=ip'
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
    text=requests.get(url=url,headers=head,proxies={'http:':'114.97.75.239:9999'}).text
    with open('./jj.html','w',encoding='utf-8') as a:
        a.write(text)