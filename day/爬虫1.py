# import requests
# import json
# if __name__ == '__main__':
#     url='https://movie.douban.com/j/search_subjects?'
#     data={'type': 'movie','tag': '热门','sort': 'recommend','page_limit': '20','page_start': '60'}
#     head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
#     req=requests.get(url=url,params=data,headers=head)
#     text=req.json()
#     fp=open('./hh.json','w',encoding='utf-8')
#     json.dump(text,fp=fp,ensure_ascii=False)


# import requests
# import json
# if __name__ == '__main__':
#     url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
#     w=input()
#     data={'cname':"",'pid':"",'keyword':w,'pageIndex':"1",'pageSize':"10"}
#     head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
#     req=requests.post(url=url,data=data,headers=head)
#     text=req.json()
#     name=w+'.json'
#     fp=open(name,'w',encoding='utf-8')
#     json.dump(text,fp=fp,ensure_ascii=False)


# import requests
# if __name__ == '__main__':
#     url='https://wallpaperm.cmcm.com/4c8e5751ebf9a301ade670bd4455397e.jpg'
#     req=requests.get(url=url).content
#     with open('./hh.jpg','wb') as a:
#         a.write(req)
import requests
import json
if __name__ == '__main__':
     Url="http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
     head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
     lis = []
     lis1 = []
     for i in range(1,2):
         i=str(i)
         data={'on': 'true',
               'page': i,
               'pageSize': '15',
               'productName': "",
               'conditionType': '1',
               'applyname':'','applysn':''
               }

         req=requests.post(url=Url,headers=head,data=data).json()

         for i in req['list']:
                lis.append(i['ID'])
     for i in lis:
          post='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
          da={
               'id':i
          }
          req1 = requests.post(url=post, headers=head, data=da).json()
          lis1.append(req1)
     fp=open('./h.json','w',encoding='utf-8')
     json.dump(lis1,fp=fp,ensure_ascii=False)






