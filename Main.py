# Railway Reservation System

seats = 50
bookings = {}
booking_counter = 1


def check_availability():
    print(f"\nAvailable seats: {seats}")


def book_ticket():
    global seats, booking_counter

    if seats <= 0:
        print("\nNo seats available!")
        return

    name = input("Enter name: ")
    age = input("Enter age: ")

    booking_id = f"B{booking_counter}"
    booking_counter += 1

    bookings[booking_id] = {
        "name": name,
        "age": age
    }

    seats -= 1

    print(f"\nTicket booked successfully!")
    print(f"Booking ID: {booking_id}")


def view_ticket():
    booking_id = input("Enter booking ID: ")

    if booking_id in bookings:
        print("\nBooking Details:")
        print(f"Name: {bookings[booking_id]['name']}")
        print(f"Age: {bookings[booking_id]['age']}")
    else:
        print("\nBooking not found!")


def cancel_ticket():
    global seats

    booking_id = input("Enter booking ID: ")

    if booking_id in bookings:
        del bookings[booking_id]
        seats += 1
        print("\nTicket cancelled successfully!")
    else:
        print("\nInvalid booking ID!")


def menu():
    while True:
        print("\n===== Railway Reservation System =====")
        print("1. Check Availability")
        print("2. Book Ticket")
        print("3. View Ticket")
        print("4. Cancel Ticket")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            check_availability()
        elif choice == '2':
            book_ticket()
        elif choice == '3':
            view_ticket()
        elif choice == '4':
            cancel_ticket()
        elif choice == '5':
            print("Exiting system...")
            break
        else:
            print("Invalid choice! Try again.")


# Run the program
menu()
