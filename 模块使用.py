#encoding=gbk   #修改文件编码
import urllib.request
print(urllib.request.urlopen('http://www.baidu.com').read())