# 与操作系统有关
import os
# os.remove('b.txt')
# os.system('cmd.exe')
# os.startfile('C:\\Program Files (x86)\\Tencent\\QQ\\Bin\\qq.exe')
# print(os.getcwd())
# lst=os.listdir('../chat')
# print(lst)
# os.mkdir('wocao')
# os.makedirs('a/b/c')
# os.rmdir('wocao')
# os.removedirs('a/b/c')
# os.chdir('C:\\Windows\\System32')
# os.system('cmd.exe')


# import os.path
# print(os.path.abspath('os模块.py'))
# print(os.path.exists('os模块.py'),os.path.exists('hhh.py'))
# print(os.path.join('B:\\python','b.by'))
# print(os.path.split("D:\\基础\\chat\\h1.py"))
# print(os.path.splitext('h1.py'))
# print(os.path.basename("D:\\基础\\chat\\h1.py"))
# print(os.path.dirname("D:\\基础\\chat\\h1.py"))
# print(os.path.isdir("D:\\基础\\chat\\h1.py"))

# dir=os.getcwd()
# path=os.listdir(dir)
# for i in path:
#     if i.endswith('.py'):
#         print(i)

# path=os.getcwd()
# lis=os.walk(path)
# for fpath,dname,fname in lis:
#     for i in dname:
#         print(os.path.join(fpath,i))
#     for i in fname:
#         print(os.path.join(fpath,i))