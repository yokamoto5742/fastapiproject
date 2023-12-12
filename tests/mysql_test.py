import mysql.connector as mydb

# コネクションを作成
cnx= mydb.connect(
    host='localhost',
    port='3306',
    user='root',
    password='gakuto57',
    database='new_db' # さっき作ったデータベース名
)

# カーソルを作成
cur = cnx.cursor()

cur.execute("insert into sample (id, name, age) values (4, 'melon', 33)")
cnx.commit()

# 全てのデータを取得・表示
cur.execute("select * from sample")
rows = cur.fetchall()
for row in rows:
    print(row)

# コネクションを閉じる
cnx.close()