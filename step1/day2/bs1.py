from bs4 import BeautifulSoup
import requests
url='https://news.naver.com'
res = requests.get(url)
print(res)
print(res.status_code)
soup = BeautifulSoup(res.content, 'html.parser')
print(soup)
print("="*100)
print(soup.prettify()) # 구조화되게 출력
# 이미지 테그만 가져오기
import os
from urllib import request
img_dir = "./images"
if not os.path.exists(img_dir):
    os.mkdir(img_dir)

img1 = soup.find('img')
# print(img1)
img_all = soup.find_all('img')
# print(img_all)
for i, v in enumerate(img_all):
    if v.get('src'):
        request.urlretrieve(v.get('src'), img_dir + str(i)+'.png')
        print(v.get('src'))
