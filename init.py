import sqlite3
# 创建一个新的数据库文件
conn = sqlite3.connect('user_system.db')
# 创建一个表
conn.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

