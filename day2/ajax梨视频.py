# -*- coding:utf-8 -*-

# import requests
# url='https://www.pearvideo.com/video_1733291'
# con=url.split('_')[1]
# urls=f'https://www.pearvideo.com/videoStatus.jsp?contId={con}&mrd=0.9664101321164462'
#
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43",
#     'Referer':url
# }
# json=requests.get(url=urls,headers=headers).json()
# ex=json["systemTime"]
# # https://video.pearvideo.com/mp4/adshort/20210625/cont-1733291-15704107_adpkg-ad_hd.mp4
# # https://video.pearvideo.com/mp4/adshort/20210625/1624622060205-15704107_adpkg-ad_hd.mp4
# mp4=json["videoInfo"]['videos']['srcUrl']
# mp4=mp4.replace(ex,f'cont-{con}')
# with open('a.mp4','wb') as f:
#     f.write(requests.get(mp4).content)

from lxml import etree
import requests
url='https://www.pearvideo.com/category_130'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43",
}
text=requests.get(url=url,headers=headers).text
tree=etree.HTML(text)
a_lst=tree.xpath('//*[@id="listvideoListUl"]/li/div')
for a in a_lst:
    h=a.xpath("./a/@href")[0]
    hh=h.split('_')[1]
    html=f'https://www.pearvideo.com/{h}'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43",
        'Referer':html
    }
    newurl='https://www.pearvideo.com/videoStatus.jsp?'
    param = {
        "contId": hh
    }
    json=requests.get(url=newurl,headers=headers,params=param).json()
    mp4 = json["videoInfo"]['videos']['srcUrl']
    ex=json["systemTime"]
    mp4=mp4.replace(ex,f'cont-{hh}')
    print(mp4)
