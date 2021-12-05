"""
Pythonでデータベースとコネクション

NoSQLの種類
・キーバリュー型 : DBM, memcach
・ドキュメント型 : MongoDB
・ワイドカラム型 : Hbase
・グラフ型      : Neo4j
"""
import sqlite3

# データベースファイルの作成
# conn = sqlite3.connect('test_sqlite.db')
# メモリー上で実行できる
conn = sqlite3.connect(':memory:')

# カーソルの作成
curs = conn.cursor()
# テーブル[persons]の作成
curs.execute(
    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
# コミットする=データベースに書き込みする
conn.commit()
# データを入れてみる
curs.execute(
    'INSERT INTO persons(name) values("SAKATAI")')
conn.commit()

# データの中身をprint()で確認する
curs.execute('SELECT * FROM persons')
# リストで返される
print(curs.fetchall())

curs.execute(
    'INSERT INTO persons(name) values("nob")')
curs.execute(
    'INSERT INTO persons(name) values("yui")')
conn.commit()

# データの上書き
curs.execute('UPDATE persons set name = "Mamoru" WHERE name = "SAKATAI"')
conn.commit()

# データの削除
curs.execute('DELETE FROM persons WHERE name = "Mamoru"')
conn.commit()

# データの中身をprint()で確認する
curs.execute('SELECT * FROM persons')
# リストで返される
print(curs.fetchall())

# 最後にデータベースとカーソルをクローズする
curs.close()
conn.close()