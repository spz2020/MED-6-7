import sqlite3
sign_in_name = 'Jessie@brawlstars.com'
password = 'password'
# 创建一个新的数据库文件
conn = sqlite3.connect('user_system.db')
# 创建一个表
conn.execute("BEGIN TRANSACTION")
conn.execute("INSERT INTO users (email, password) VALUES (?, ?)", (sign_in_name, password)) 
conn.commit()