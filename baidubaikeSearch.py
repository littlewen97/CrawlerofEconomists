import re
import bs4
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
import sys

file_read = open('economist.txt',encoding='UTF-8')
file_write = open("baike_url.txt", 'w',encoding='UTF-8')
for line in file_read.readlines():
    search_item = line.strip()
    print(search_item)
    try:
        url = 'https://baike.baidu.com/item/' + urllib.parse.quote(search_item)
        html = urllib.request.urlopen(url)
        print("查看响应 url 地址：\n", html.geturl())
        file_write.write(html.geturl())
        file_write.write('\n')
    except AttributeError:
        print("Failed!Please enter more in details!")
