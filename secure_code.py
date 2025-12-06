import sqlite3

# Secure Coding Practice - Preventing SQL Injection

username = input("Enter username: ")
password = input("Enter password: ")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Using parameterized query (Safe)
query = "SELECT * FROM users WHERE username=? AND password=?"
cursor.execute(query, (username, password))

result = cursor.fetchall()

if result:
    print("Login Successful!")
else:
    print("Invalid Username or Password")

conn.close()
