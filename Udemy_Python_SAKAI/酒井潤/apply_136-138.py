"""
MySQL
"""
import mysql.connector


conn = mysql.connector.connect(host='127.0.0.1', user='root', password=None)

cursor = conn.cursor()

cursor.execute('CREATE DATABASE test_mysql_database')

cursor.close()
conn.close()