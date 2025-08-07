import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Poorni21@21",  # 🔒 replace with your actual MySQL password
        database="mysql"           # default system database just to test connection
    )

    if connection.is_connected():
        print("✅ Successfully connected to MySQL!")

except mysql.connector.Error as e:
    print("❌ Error connecting to MySQL:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("🔌 MySQL connection closed.")
