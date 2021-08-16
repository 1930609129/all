# def a(x):
#     b=0
#     d=len(x)-1
#     for f in range(d):           #待修改
#         c = 0
#         for i in x:
#             if c<d:
#                 if i>x[x.index(i)+1]:
#                     b = x[x.index(i) + 1]
#                     x[x.index(i)+1]=i
#                     x[x.index(i)]=b
#                     c += 1
#                 else:
#                     c+=1
#     print(x)
# b=[3,8,6,2,1,9,7,11,5]
# a(b)
# import re
# url="""<div class="thumb">
#
# <a href="/article/124382351" target="_blank">
# <img src="//pic.qiushibaike.com/system/pictures/12438/124382351/medium/ERE2VJ3RCDSCL1SI.jpg" alt="糗事#124382351" class="illustration" width="100%" height="auto">
# </a>
# </div>
#
# """
# req='<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
# a=re.findall(req,url,re.S)
# print(a)

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{i}*{j}=",i*j ,end='\t')
#     print()

import numpy
# a=[[[1,2]],
#    [[2,3]]]
# a=numpy.array(a)
# print(a.shape)
a=[[[1,2],[1,2],[1,2],[1,2]],
   [[2,3],[1,2],[1,2],[1,2]],
   [[1,2],[1,2],[3,4],[3,5]],
   [[2,3],[1,2],[3,4],[3,4]]]
a=numpy.array(a)
print(a.shape)
b=a[2:4,2:4]
c=a[2,3]
print(c)
print(b)
