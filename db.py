import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Poorni21@21",   # replace with your MySQL password
        database="bus_booking"
    )
