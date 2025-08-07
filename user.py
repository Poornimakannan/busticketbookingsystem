from db import get_connection

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        print("✅ Registration successful!")
    except:
        print("❌ Username already exists.")
    conn.close()

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        print("✅ Login successful!")
        return user[0]  # return user ID
    else:
        print("❌ Invalid credentials.")
        return None
