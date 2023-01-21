import sqlite3

#Create users
def create_db(username, password):
    #Classic sqllite operations.
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    create_table = """CREATE TABLE IF NOT EXISTS users (username, password)"""
    #Question marks are placed to prevent sqli vulnerability.
    input_users = """INSERT INTO users (username, password) VALUES (?,?)"""

    cursor.execute(create_table)
    #Here we add the username and password values ​​that we have obtained from the register.html file to the db.
    cursor.execute(input_users, (username, password))
    conn.commit()