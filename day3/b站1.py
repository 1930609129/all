import requests
import os
from lxml import etree
import re
if __name__ == '__main__':
    url=input("网址:")
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43",
        "referer": url
    }
    response=requests.get(url,headers=headers).text
    tree=etree.HTML(response)
    title=tree.xpath('//title/text()')[0].split('_')[0]
    title=title[1:-1]
    html=tree.xpath('//script[contains(text(),"window.__playinfo__")]/text()')[0]
    urls=re.findall(r'"video":\[{"id":\d+,"baseUrl":"(.*?)"',html)[0]
    aud=re.findall(r'"audio":\[{"id":\d+,"baseUrl":"(.*?)"',html)[0]
    response_video=requests.get(urls,headers=headers).content
    response_audio=requests.get(aud,headers=headers).content
    title1=title+'!'
    with open(f'{title1}.mp4','wb') as f:
        f.write(response_video)
    with open(f'{title1}.mp3','wb') as f:
        f.write(response_audio)

    os.system(f'ffmpeg -i "{title1}.mp4" -i "{title1}.mp3" -c copy "{title}.mp4"')
    os.remove(f'{title1}.mp4')
    os.remove(f'{title1}.mp3')