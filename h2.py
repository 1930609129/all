# for g in range(1,10):
#     for t in range(1,g+1):
#         print(g,'*',t,'=',g*t ,end="\t")  #end=‘\t’末尾不换行，加空格  end默认值为\n
#     print()
# def a(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# print(a(9,7))
# i = int(input())
# a=1
# b=1
# c=1
# while(i>2):
#     c=a+b
#     a=b
#     b=c
#     i-=1
# print(c)
# def h(max):
#     a,b=0,1
#     i=1
#     c=0
#     if max==1:
#         return 1
#     while i<max:
#         c=a+b
#         a=b
#         b=c
#         i+=1
#     return c
# print(h(2))
# def a(x):
#     if x==1:
#         return 1
#     else:
#         return x*a(x-1)
# print(a(4))
# r=range(1,10,2)
# print(list(r))

# for i in lis:
#     if i >lis[lis.index(i)+1]:
#         lis[lis.index(i)]=lis[lis.index(i)+1]
#     else:
#         break

# import time
# for i in range(1,101):
#     time.sleep(0.5)
#     print(f'\r{i}%',end='')

# lst=[1,2,34,5]
# s=lst[0]
# for i in lst:
#     if i>s:
#         s=i
# print(s)
# print(max(lst))
# print(min(lst))


# a="”刚从叙利亚打工回来，气质还没来得及跟上”"
# a=a[1:-1]
# print(a)