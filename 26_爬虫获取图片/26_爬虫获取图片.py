# import requests

# def get_images():
#     url = "https://api.bilibili.com/x/web-interface/dynamic/region?ps=12&rid=1"
#     header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
#     response = requests.get(url,headers = header)
#     for i in response.json().get("data").get("archives"):
#         img_url = i.get("pic")
#         img = requests.get(img_url,headers = header)
#         id = i.get("bvid")
#         with open(f"./26_爬虫获取图片/img/{id}.jpg","wb") as f:
#             f.write(img.content)

# if __name__ == '__main__':
#     get_images()
import requests

url = 'https://api.bilibili.com/x/web-interface/history/cursor?max=0&view_at=0&business='
headers = {
    'Cookie':'_uuid=392...',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
resp = requests.get(url, headers = headers)

for i in resp.json().get('data').get('list'):
    tupian_url = i.get('cover')
    name = i.get('title')
    tp_resp = requests.get(tupian_url, headers = headers)
    with open(f'{name}.jpg', 'wb') as f: # 若文件名中有斜杠则无法保存
        f.write(tp_resp.content)