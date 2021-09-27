# 1. 编写爬虫，获取B站首页动画的页面数据
# 2. 编写爬虫，获取B站首页番剧排行榜首页的数据

import requests

def get_Homepage(url:str,header1:str):
    response = requests.get(url,headers=header1)
    print(response.text)

def get_Rank(url:str,header1:str):
    response = requests.get(url,header1)
    for i,info in enumerate(response.json().get("result").get("list")):
        print(f'第{i+1}名的番剧是{info.get("title")},点击追番：{info.get("url")}')

if __name__ == "__main__":
    header1 = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    url1 = "https://www.bilibili.com/v/douga"
    url2 = "https://api.bilibili.com/pgc/web/rank/list?season_type=1&day=3"
    get_Homepage(url1,header1)
    get_Rank(url2,header1)
