from db import get_connection

def book_ticket(user_id):
    bus_id = int(input("Enter Bus ID to book: "))
    seats = int(input("How many seats to book? "))
    
    conn = get_connection()
    cursor = conn.cursor()

    # Check available seats
    cursor.execute("SELECT seats FROM buses WHERE id = %s", (bus_id,))
    result = cursor.fetchone()
    if not result:
        print("❌ Bus not found.")
        return
    available_seats = result[0]

    if seats > available_seats:
        print(f"❌ Only {available_seats} seats available.")
    else:
        cursor.execute("INSERT INTO bookings (user_id, bus_id, seats_booked) VALUES (%s, %s, %s)",
                       (user_id, bus_id, seats))
        cursor.execute("UPDATE buses SET seats = seats - %s WHERE id = %s", (seats, bus_id))
        conn.commit()
        print("✅ Booking confirmed.")
    conn.close()

def view_my_bookings(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT b.bus_name, b.source, b.destination, k.seats_booked
                      FROM bookings k
                      JOIN buses b ON k.bus_id = b.id
                      WHERE k.user_id = %s""", (user_id,))
    bookings = cursor.fetchall()
    print("\nYour Bookings:")
    for booking in bookings:
        print(f"Bus: {booking[0]} | From: {booking[1]} | To: {booking[2]} | Seats: {booking[3]}")
    conn.close()
