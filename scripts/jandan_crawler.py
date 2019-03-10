import re
import urllib.request
from urllib.error import URLError

def crawl():
    html = urllib.request.urlopen('http://jandan.net/page/1').read()
    html = str(html)
    pattern1 = '<div id="content">.*<div class="post f" style="padding-left:210px;">'
    result1 = re.compile(pattern1).findall(html)
    result1 = result1[0]
    pattern2 = '<img src="//(.+?\.jpg)!custom" width="175" height="98" />'
    imglist = re.compile(pattern2).findall(result1)
    
    # 添加请求头信息
    opener = urllib.request.build_opener()
    opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36")]
    urllib.request.install_opener(opener)

    x = 1
    for imgurl in imglist:
        imgname = "E:/img/" + str(x) + ".jpg"
        imgurl = "http://" + imgurl
        try:
            urllib.request.urlretrieve(imgurl, imgname, )
        except URLError as e:
            print(e)
        finally:
            x += 1

if __name__ == '__main__':
    crawl()
