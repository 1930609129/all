import requests
import re
import os
if not os.path.exists('./hhh/'):
    os.mkdir('./hhh/')
if __name__ == '__main__':
    url='https://m.3gbizhi.com/meinv/mn15%d_%d.html'
    c=int(input())
    for a in range(1,3):
        new=format(url%(c,a))
        head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
        text=requests.get(url=new,headers=head).text
        req='<div class="cont pos showpic">.*?<img src="(.*?)" alt.*?</div>'
        lis=re.findall(req,text,re.S)
        ipg = requests.get(url=lis[0], headers=head).content
        a=str(a)
        name='./hhh/'+a+'.jpg'
        with open(name,'wb') as b:
            b.write(ipg)
#cont pos showpic