import urllib.request
import re

class gethtml():
    def __init__(self,url,head):
        self.url=url
        self.head=head
    def getindex(self):
        self.requst=urllib.request.Request(self.url)
        self.requst.add_header("user-agent",self.head)
        self.response=urllib.request.urlopen(self.requst)
        return self.response.read()
    def getlist(self):
        self.biglist=[]
        self.imglist=re.findall(b"",self.getindex())   #b""加上链接
        for i in self.imglist:
            self.biglist.append(self.url+str(i,encoding="utf8"))
        return self.biglist
    def getimage(self):
        mun=0
        for self.url in self.getlist():
            mun+=1
            with open(str(mun)+".jpg","wb") as f:
                f.write(self.getindex())
html=gethtml("","")     #加上链接
html.getimage()