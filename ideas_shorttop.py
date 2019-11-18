import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

def download(url, num_retries=2, user_agent='wswp', proxies=None):
    '''下载一个指定的URL并返回网页内容
        参数：
            url(str): URL
        关键字参数：
            user_agent(str):用户代理（默认值：wswp）
            proxies（dict）： 代理（字典）: 键：‘http’'https'
            值：字符串（‘http(s)://IP’）
            num_retries(int):如果有5xx错误就重试（默认：2）
            #5xx服务器错误，表示服务器无法完成明显有效的请求。
            #https://zh.wikipedia.org/wiki/HTTP%E7%8A%B6%E6%80%81%E7%A0%81
    '''
    print('==========================================')
    print('Downloading:', url)
    headers = {'User-Agent': user_agent} #头部设置，默认头部有时候会被网页反扒而出错
    try:
        resp = requests.get(url, headers=headers, proxies=proxies) #简单粗暴，.get(url)
        html = resp.text #获取网页内容，字符串形式
        if resp.status_code >= 400: #异常处理，4xx客户端错误 返回None
            print('Download error:', resp.text)
            html = None
            if num_retries and 500 <= resp.status_code < 600:
                # 5类错误
                return download(url, num_retries - 1)#如果有服务器错误就重试两次

    except requests.exceptions.RequestException as e: #其他错误，正常报错
        print('Download error:', e)
        html = None
    return html #返回html

def get_table(html):
    soup = BeautifulSoup(html, 'html.parser')

    #获取经济学家的姓名
    name = []
    names = soup.select('.shorttop td:nth-child(2)>a:nth-child(1)')
    for item in names:
        name.append(item.text)

    #获取经济学家隶属的机构
    department1 = []
    department2 = []
    departments = soup.select('.shorttop td:nth-child(2) p')
    for item in departments:
        item = str(item)
        string = item.split('<br/>')
        if len(string) == 1:
            string1 = re.sub(r'\<.*?\>', "", string[0])
            department1.append(string1)
            department2.append('')
        if len(string) == 2:
            string1 = re.sub(r'\<.*?\>', "", string[0])
            string2 = re.sub(r'\<.*?\>', "", string[1])
            department1.append(string1)
            department2.append(string2)

    if len(name)==len(department1)==len(department2):
        # 字典中的key值即为csv中列名
        dataframe = pd.DataFrame({'Name':name, 'Institution1': department1, 'Institution2': department2})
        # 将DataFrame存储为csv,index表示是否显示行名，default=True
        dataframe.to_csv(r"top2858.csv", sep=',')
        print("success!")

html = download('https://ideas.repec.org/top/top.person.all.html')
get_table(html)