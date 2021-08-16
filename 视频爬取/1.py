import requests
import re
url='https://www.91kanju.com/vod-play/59444-1-1.html'
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}
text=requests.get(url=url,headers=head).text
h=re.compile(r"url: '(?P<url>.*?)',",re.S)
m3u8_url=h.search(text).group('url')
print(m3u8_url)
# text=requests.get(url=m3u8_url,headers=head).text
# with open('./1.m3u8','w') as f:
#     f.write(text)
