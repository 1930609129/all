import requests
import re
import os
if not os.path.exists('./hhh'):
    os.mkdir('./hhh')
if __name__ == '__main__':

    url='https://www.qiushibaike.com/imgrank/page/%d/'
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
    for j in range(1,5):
        newurl=format(url%j)
        text = requests.get(url=newurl, headers=head).text
        req='<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        h = re.findall(req, text, re.S)
        for i in h:
            http='https:'+i
            file=http.split('/')[-1]
            ipg=requests.get(url=http,headers=head).content
            name='./hhh/'+file
            with open(name,'wb') as a:
                a.write(ipg)
