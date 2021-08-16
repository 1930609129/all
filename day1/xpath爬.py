import requests
from lxml import etree
if __name__ == '__main__':
    url='https://www.aqistudy.cn/historydata/'
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}

    text=requests.get(url=url,headers=head).text
    tree=etree.HTML(text)
    list=tree.xpath('//div[@class="bottom"]/ul/li')

    host=[]
    allcity=[]
    for li in list:
        hot=li.xpath('./a/text()')[0]
        host.append(hot)
    all=tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    for li in all:
        city=li.xpath('./a/text()')[0]
        allcity.append(city)
    print(host)
    print(allcity)

    # url = 'https://www.aqistudy.cn/historydata/'
    # head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
    # allci=[]
    # text = requests.get(url=url, headers=head).text
    # tree = etree.HTML(text)
    # all = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')
    # for a in all:
    #     allhot=a.xpath('./text()')[0]
    #     allci.append(allhot)
    # print(allci)