from lxml import etree
import requests

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
def get_courses():
    url = "https://www.itbaizhan.com/"
    response  = requests.get(url,headers = header)
    e = etree.HTML(response.text)
    info = e.xpath("//ul[@class=\"clearfix\"]/li/a/text()")
    print(info)

def get_rank():
    url = "https://www.bilibili.com/v/popular/rank/bangumi?spm_id_from=333.851.b_62696c695f7265706f72745f616e696d65.51"
    response = requests.get(url, headers = header)
    e = etree.HTML(response.text)
    names = e.xpath("//a[@class=\"title\"]/text()")
    plays = e.xpath("//span[@class=\"data-box\"][1]/text()")
    favs = e.xpath("//span[@class=\"data-box\"][3]/text()")
    i = 0
    for name,play,fav in zip(names,plays,favs):
        i += 1
        print(f"排名：{i}，番剧名称：{name}，播放量：{play.strip()}，收藏量：{fav.strip()}")

if __name__ == "__main__":
    get_courses()
    get_rank()