# import requests
# from bs4 import BeautifulSoup
# import re
# import time
# if __name__ == '__main__':
#     url='https://www.3gbizhi.com/mttag/xiaojiejie/'
#     head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
#     req=requests.get(url=url,headers=head).text
#     beau=BeautifulSoup(req,'lxml')
#     li_lis=beau.find_all('li')
#     for j in li_lis:
#         http=j.a['href'].endswith('.html')
#         if http:
#             text = requests.get(url=j.a['href'], headers=head).text
#             req2 = '<div class="showcontw mtw">.*?<img src="(.*?)" id.*?</div>'
#             lis = re.findall(req2, text, re.S)
#             ipg = requests.get(url=lis[0], headers=head).content
#             name = './hhh/' + str(time.time()) + '.jpg'
#             with open(name, 'wb') as b:
#                 b.write(ipg)

# import requests
# from bs4 import BeautifulSoup
# if __name__ == '__main__':
#     url='https://www.shicimingju.com/book/sanguoyanyi.html'
#     head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
#     req=requests.get(url=url,headers=head).text.encode('iso-8859-1')
#     baeu=BeautifulSoup(req,'lxml')
#     text=baeu.select('.book-mulu > ul >li')
#     fp=open('./sg.txt','w',encoding='utf-8')
#     for i in text:
#         title=i.a.string
#         https='https://www.shicimingju.com'+i.a['href']
#         wb=requests.get(url=https,headers=head).text.encode('iso-8859-1')
#         wbbaeu=BeautifulSoup(wb,'lxml')
#         nr=wbbaeu.find('div',class_='chapter_content')
#         wbnr=nr.text
#         fp.write(title+':'+wbnr+'.\n')
