# import re
# url="""<div class="cont pos showpic">
# 				<a href="https://m.3gbizhi.com/meinv/mn1541_9.html" class="pverleft"></a>
# 				<a href="https://m.3gbizhi.com/meinv/mn1540_2.html" class="nextright"></a>
# 				<a href="https://m.3gbizhi.com/meinv/mn1540_2.html"><img src="https://pic.3gbizhi.com/2020/1220/20201220074041689.jpg" alt="身材苗条漂亮美少女吊带衣 死库水教室写真图片" style="background: url(https://pic.3gbizhi.com/2020/1220/thumb_200_0_20201220074041689.jpg) no-repeat; background-size:100%;"></a>
# 			</div>"""
# req='<div class="cont pos showpic">.*?<img src="(.*?)" alt.*?</div>'
# a=re.findall(req,url,re.S)
# print(a)

import requests
from lxml import etree

url='https://www.kanxiaojiejie.com/archives/3447'
head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
t=requests.get(url=url,headers=head).text
tree=etree.HTML(t)
lst=tree.xpath('//*[@id="page"]/div/div/div/div[1]/div/article')
for i in lst:
    jpg=i.xpath('./div/div/a/img/@src')
    print(jpg)