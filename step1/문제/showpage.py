import requests
from bs4 import BeautifulSoup

idx = input("검색할 단어를 입력하세요: ")

url = 'https://search.danawa.com/dsearch.php?query=' + str(idx)
res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')

print(url)
print(res)
print(soup)

# div = soup.find('div', class_='list_content')
# lis = div.find_all('li')
# for i, li in enumerate(lis):
#     if i > 0:
#         category = li.find('span', class_='colName').text
#         r_dt = li.find('span', class_='colDate').text
#         hit = li.find('span', class_='colHit').text
#         a = li.find('span', class_='colSbj-cate').find_all('a')[0]
#         url = a.get('href')
#         title = a.text
#         print(url, title, category, hit, r_dt)