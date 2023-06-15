import requests
import json

url = 'https://api.upbit.com/v1/market/all'
res = requests.get(url)
json_data = res.json()  # JSON 데이터를 파싱하여 변수에 저장

print(json_data)

for row in json_data:
    print(row['market'], row['korean_name'], row['english_name'])


import sqlite3

conn = sqlite3.connect('stock.db')
# 순서 매핑
sql1 = """INSERT INTO stock VALUES (?, ?, ?)"""
cur = conn.cursor()

for row in json_data:
    cur.execute(sql1, [row['market'], row['korean_name'], row['english_name']])

conn.commit()
conn.close()