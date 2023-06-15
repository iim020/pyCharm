import cx_Oracle

conn = cx_Oracle.connect('C##jsp', 'oracle', 'localhost:1521/xe')
print(conn.version)

nm = input("검색할 이름을 입력해주세요: ")
param = {"nm": '%' + nm + '%'}

with conn:
    cur = conn.cursor()
    sql = """SELECT * FROM member WHERE mem_name LIKE :nm"""
    rows = cur.execute(sql, param)
    for r in rows:
        print(r)
