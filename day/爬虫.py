# import requests
#
# if __name__ == '__main__':
#     url='https://www.baidu.com/'
#     pa=requests.get(url=url)
#     rp=pa.text
#     print(rp)
#     with open("./day.html",'w',encoding='utf-8') as a:
#         a.write(rp)


# import requests
# if __name__ == '__main__':
#     url='https://www.baidu.com/s?'
#     ww=input()
#     kw={'wd':ww}
#     head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
#     req= requests.get(url=url, params=kw, headers=head)
#     text=req.text
#     file=ww+'.html'
#     with open(file,'w',encoding='utf-8') as a:
#         a.write(text)

import requests
import json
if __name__ == '__main__':
    url='https://fanyi.baidu.com/sug'
    w=input()
    da={'kw':w}
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
    req=requests.post(url=url,data=da,headers=head)
    text=req.json()
    name=w+'.json'
    file=open(name,'w',encoding='utf-8')
    json.dump(text,fp=file,ensure_ascii=False)  #ensure_ascii=False解决中文
