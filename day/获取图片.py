import requests
import re
import os
# if __name__ == '__main__':
#     url='https://www.3gbizhi.com/mttag/xiaojiejie/'
#     head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
#     text=requests.get(url=url,headers=head).text
#     req = '<div class="img">src="(.*?)"srcset.*?</div>'
#     h=re.findall(req,text,re.S)
if not os.path.exists('./hhhh'):
    os.mkdir('./hhhh')
if __name__ == '__main__':
    url='https://www.qiushibaike.com/imgrank/'
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
    text = requests.get(url=url, headers=head).text
    req='<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    h = re.findall(req, text, re.S)

    for i in h:
        http='https:%s'%i
        file=http.split('/')[-1]
        ipg=requests.get(url=http,headers=head).content
        name='./hhhh/%s'%file
        with open(name,'wb') as a:
            a.write(ipg)

