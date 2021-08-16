import requests
import os
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43",
    "referer": "https://www.bilibili.com/video/BV185411M7jw?t=9"
}
url1='https://cn-gdgz4-cmcc-v-14.bilivideo.com/upgcxcode/12/96/348229612/348229612_nb2-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1624779694&gen=playurlv2&os=vcache&oi=2028416525&trid=0001a52e1415f40f46e5b1946bb825fe845au&platform=pc&upsig=d8841c07ab0f2fe65dbaae05fd606548&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&cdnid=11307&mid=505118099&bvc=vod&orderid=0,3&agrr=1&logo=80000000'
url2='https://cn-gdgz4-cmcc-v-02.bilivideo.com/upgcxcode/12/96/348229612/348229612_nb2-1-30080.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1624779694&gen=playurlv2&os=vcache&oi=2028416525&trid=0001a52e1415f40f46e5b1946bb825fe845au&platform=pc&upsig=59b2f044f425f280af1ca071235552c6&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&cdnid=2003&mid=505118099&bvc=vod&orderid=0,3&agrr=1&logo=80000000'
"""https://cn-gdgz4-cmcc-v-02.bilivideo.com/upgcxcode/12/96/348229612/348229612_nb2-1-30080.m4s?
https://cn-gdgz4-cmcc-v-14.bilivideo.com/upgcxcode/12/96/348229612/348229612_nb2-1-30280.m4s?
"""

if __name__ == '__main__':

    mp4=requests.get(url2,headers=headers).content
    mp4_1=requests.get(url1,headers=headers).content

    with open('a.mp4','wb') as f:
        f.write(mp4)
    with open('a1.mp3','wb') as f:
        f.write(mp4_1)

    os.system('ffmpeg -i "a.mp4" -i "a1.mp3" -c copy "hh.mp4"')
