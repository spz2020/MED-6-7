import sqlite3

sign_in_name = 'Jessie@brawlstars.com'
password = 'password'

conn = sqlite3.connect('database/user_system.db')

conn.execute("BEGIN TRANSACTION")
conn.execute("INSERT INTO users (email, password) VALUES (?, ?)", (sign_in_name, password)) 
conn.commit()