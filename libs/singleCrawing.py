# -*- coding:utf-8 -*-
import ssl
import urllib.request

import re

ssl._create_default_https_context = ssl._create_unverified_context

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    reg = r'src="(.[^>]+?\.jpg)" size'
    imgre = re.compile(reg)
    html = html.decode('utf-8')

    imglist = re.findall(imgre, html)

    x = 0

    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '/Users/zhangmeng/Desktop/Test/%s.jpg' % x)
        x += 1


html=getHtml("https://tieba.baidu.com/p/6125750359")
print(getImg(html))