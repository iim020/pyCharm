import requests
from bs4 import BeautifulSoup
import cx_Oracle
import sqlite3

conn = cx_Oracle.connect('C##jsp', 'oracle', 'localhost:1521/xe')

sql = """merge into musinsa a
         using dual b
         on (a.sql = :sql)
         when matched then -- 있을 경우
             update set a.hit = :hit,
                        a.r_dt = :r_dt
         when not matched then -- 없을 경우
             insert values (:sql, :title, :cate, :hit, :r_dt, :detail_url)"""

with conn:
    for idx in range(1, 100):
        url = 'https://www.musinsa.com/mz/community?p=' + str(idx)
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')
        div = soup.find('div', class_='list_content')
        lis = div.find_all('li')
        for i, li in enumerate(lis):
            if i > 0:
                category = li.find('span', class_='colName').text
                r_dt = li.find('span', class_='colDate').text
                hit = li.find('span', class_='colHit').text
                a = li.find('span', class_='colSbj-cate').find_all('a')[0]
                url = a.get('href')
                title = a.text
                data = {"sql": url, "title": title, "cate": category, "hit": hit, "r_dt": r_dt, "detail_url": url}
                cur = conn.cursor()
                cur.execute(sql, data)
                conn.commit()
                print(sql, title, category, hit, r_dt, url)
