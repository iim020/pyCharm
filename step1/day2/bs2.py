from bs4 import BeautifulSoup
import requests
import re
# 영화 제목, 링크정보, 점수, 관객수, 이미지 경로
url='https://movie.daum.net/ranking/boxoffice/weekly'
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
lis = soup.select('.box_boxoffice .list_movieranking li')
arr = []
for li in lis:
    print('=' * 100)
    a = li.select_one('.tit_item a')
    title = a.getText()
    movie_url = a.get('href')
    infos = li.select('.txt_info .info_txt')
    score = re.sub(r'[^0-9,]','',infos[1].getText())
    print(infos[1].getText)
    img =li.select_one('img').get('src')
    arr.append([title, score, movie_url, img])
    import  csv
with open('movie.csv','w',newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter='|')
    writer.writerows(arr)
    # print(a.get('href'), a.getText())
    # print(li)
