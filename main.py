from user import register, login
from bus import add_bus, view_buses
from booking import book_ticket, view_my_bookings

def main():
    print("🚍 Welcome to Bus Ticket Booking System")
    
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose option: ")
        
        if choice == '1':
            register()
        elif choice == '2':
            user_id = login()
            if user_id:
                while True:
                    print("\n1. View Buses\n2. Book Ticket\n3. My Bookings\n4. Add Bus (Admin)\n5. Logout")
                    op = input("Choose option: ")
                    if op == '1':
                        view_buses()
                    elif op == '2':
                        book_ticket(user_id)
                    elif op == '3':
                        view_my_bookings(user_id)
                    elif op == '4':
                        add_bus()
                    elif op == '5':
                        break
        elif choice == '3':
            print("Thank you for using the system.")
            break

main()
