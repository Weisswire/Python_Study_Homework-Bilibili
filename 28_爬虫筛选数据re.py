import re
import requests

def get_rank():
    url = "https://www.bilibili.com/v/popular/rank/bangumi?spm_id_from=333.851.b_62696c695f7265706f72745f616e696d65.51"
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url,headers = header)
    names = re.findall('le\">(.+)</a',response.text)
    # 运用[\u4e00-\u9fa5]匹配单个汉字
    plays = re.findall('''play"></i>
              (.+[\u4e00-\u9fa5])
            ''',response.text)
    favs = re.findall('''fav"></i>
              (.+[\u4e00-\u9fa5])
            ''',response.text)
    url_head = "https://api.bilibili.com/pgc/web/season/stat?season_id="
    urls_tile = re.findall("<a href=\"//www.bilibili.com/bangumi/play/ss(.+)\" target=\"_blank\">",response.text)
    likes = []
    for url_tile in urls_tile:
        resp = requests.get(url_head+url_tile,headers=header)
        info = resp.json().get("result").get("likes")
        likes.append(info)
    i = 0
    for name,play,fav,like in zip(names,plays,favs,likes):
        i += 1
        print(f'排名：{i}，番剧名称：{name}，播放量：{play}，追番数：{fav}，点赞数：{like}')

if __name__ == "__main__":
    get_rank()