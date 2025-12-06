import sqlite3

# Hardcoded credentials vulnerability
username = input("Enter username: ")
password = input("Enter password: ")

# SQL Injection vulnerability (unsafe string formatting)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
print("Executing Query:", query)

cursor.execute(query)
result = cursor.fetchall()

if result:
    print("Login Successful!")
else:
    print("Invalid Username or Password")
