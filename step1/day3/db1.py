import sqlite3

db_file = 'stock.db'  # 사용할 파일명 지정

conn = sqlite3.connect(db_file)  # 파일명을 인자로 전달하여 데이터베이스에 연결
cur = conn.cursor()

sql = """
    CREATE TABLE stock (
        code VARCHAR(100),
        kor_nm VARCHAR(100),
        en_nm VARCHAR(100)
    )
"""

cur.execute(sql)
