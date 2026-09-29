from main import BusinessAutomationSystem


def main():
    system = BusinessAutomationSystem()

    while True:
        print("\n=== Business Automation System ===")
        print("1. Add customer")
        print("2. Create booking")
        print("3. View bookings")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Customer name: ")
            phone = input("Phone number: ")

            system.add_customer(name, phone)
            print("Customer added successfully.")

        elif choice == "2":
            customer = input("Customer name: ")
            service = input("Service: ")
            date = input("Booking date (YYYY-MM-DD): ")

            system.create_booking(customer, service, date)
            print("Booking created successfully.")

        elif choice == "3":
            print("\n--- Bookings ---")
            system.show_bookings()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
