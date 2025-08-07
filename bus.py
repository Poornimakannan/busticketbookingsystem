from db import get_connection

def add_bus():
    name = input("Enter bus name: ")
    source = input("Enter source: ")
    destination = input("Enter destination: ")
    seats = int(input("Enter total seats: "))
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO buses (bus_name, source, destination, seats) VALUES (%s, %s, %s, %s)",
                   (name, source, destination, seats))
    conn.commit()
    conn.close()
    print("✅ Bus added successfully.")

def view_buses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM buses")
    buses = cursor.fetchall()
    print("\nAvailable Buses:")
    for bus in buses:
        print(f"ID: {bus[0]} | Name: {bus[1]} | From: {bus[2]} | To: {bus[3]} | Seats: {bus[4]}")
    conn.close()
