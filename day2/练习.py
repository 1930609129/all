# -*- coding:utf-8 -*-
# data={
# 	"resultCode":"1",
# 	"resultMsg":"success", "reqId":"b4700643-5a67-49d2-9660-2e511a49b2f1",
# 	"systemTime": "1622642017734",
# 	"videoInfo":{"playSta":"1","video_image":"https://image2.pearvideo.com/cont/20210504/15317924-164310-1.png","videos":{"hdUrl":"","hdflvUrl":"","sdUrl":"","sdflvUrl":"","srcUrl":"https://video.pearvideo.com/mp4/third/20210504/1622642017734-15317924-164036-hd.mp4"}}
# }
# print(data['videoInfo']['videos']['srcUrl'])

# import requests
# from lxml import etree
# url='https://www.kanxiaojiejie.com/'
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
# text=requests.get(url=url,headers=head).text
# tree=etree.HTML(text)
# lis=tree.xpath('//*[@id="masonry"]')
# for a in lis:
#     src = a.xpath('//@src')
#     for a in src:
#         if a.endswith('.jpg'):
#             print(a)

# import requests
# from lxml import etree
# url='https://www.kanxiaojiejie.com/'
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
# text=requests.get(url=url,headers=head).text
# tree=etree.HTML(text)
# lis=tree.xpath('//*[@id="masonry"]/article')
# for a in lis:
#     src = a.xpath('.//a/img/@src')
#     print(src)


# import requests
# from lxml import etree
# url='https://www.kanxiaojiejie.com/page/%d'
# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
# for i in range(1):
#     newurl=format(url%i)
#     text=requests.get(url=newurl,headers=head).text
#     tree=etree.HTML(text)
#     lis=tree.xpath('//*[@id="masonry"]/article')
#     for a in lis:
#         src = a.xpath('./div/div/a/img/@src')[0]
#         name=src.rsplit(sep="/",maxsplit=1)[-1]
#         fp='./hhh/'+name
#         jpg=requests.get(url=src,headers=head).content
#         with open(fp,'wb') as a:
#             a.write(jpg)


import requests
from lxml import etree
url='https://www.3gbizhi.com/meinv/index_0.html'
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
text=requests.get(url=url,headers=head).text
tree=etree.HTML(text)
a_lst=tree.xpath('/html/body/div[5]/ul/li/a')
lst=[]
for a in a_lst:
    h=a.xpath('./@href')
    lst.append(h)
print(lst)