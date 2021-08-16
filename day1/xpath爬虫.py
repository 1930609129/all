# import requests
# from lxml import etree
# if __name__ == '__main__':
#     url='https://bj.58.com/ershoufang/'
#     head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
#     text=requests.get(url=url,headers=head).text
#     tree=etree.HTML(text)
#     list=tree.xpath('//section[@class="list"]/div')
#     fp=open('./bj.txt','w',encoding='utf-8')
#     for li in list:
#         t=li.xpath('.//h3/text()')[0]
#         fp.write(t+'\n')


# import requests
# from lxml import etree
# import os
# if __name__ == '__main__':
#     url='https://pic.netbian.com/4kmeinv/'
#     head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
#     # req=requests.get(url=url,headers=head)
#     # req.encoding='utf-8'
#     # text = req.text
#     text=requests.get(url=url,headers=head).text.encode('iso-8859-1')
#     # requests.get(url=url, headers=head).text.encode('iso-8859-1').decode('gbk')  解决中文乱码
#     tree=etree.HTML(text)
#     list=tree.xpath('//ul[@class="clearfix"]/li')
#     if not os.path.exists('./hhh'):
#         os.mkdir('./hhh')
#     for li in list:
#         jpg='https://pic.netbian.com'+li.xpath('./a/img/@src')[0]
#         name=li.xpath('./a/img/@alt')[0]+'.jpg'
#         mmjpg=requests.get(url=jpg,headers=head).content
#         path='hhh/'+name
#         with open(path,'wb') as a:
#             a.write(mmjpg)