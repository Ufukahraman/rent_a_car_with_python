from app import carRent, bikeRent, customer

bike = bikeRent(100)
car = carRent(10)
customer_obj = customer()

main_menu = True

while True:
    if main_menu:
        print("""
        ********* Vehicle Rental Shop*********

        A. Bike Rent
        B. Car Rent
        Q. Exit

        **************************************
        """)
        main_menu = False
    choice = input("Enter choice : ")

    if choice.lower() == "a":
        print("""
        *********** BIKE Menu **************
        1. Display available bikes
        2. Request a bike on hourly basis $5
        3. Request a bike on daily basis $84
        4. Return a bike
        5. Main menu
        6. Exit
        ************************************
        """)
        choice = input("Enter choice")

        try:
            choice = int(choice)
        except ValueError:
            print("Please enter a valid number : ")
            continue

        if choice == 1:
            bike.displayStock()
        elif choice == 2:
            customer_obj.rentalTime_b = bike.rentHourly(customer_obj.requestVehicle("bike"))
            customer_obj.rentalBasis_b = 1
            main_menu = True
        elif choice == 3:
            customer_obj.rentalTime_b = bike.rentDaily(customer_obj.requestVehicle("bike"))
            customer_obj.rentalBasis_b = 2
            main_menu = True
        elif choice == 4:
            customer_obj.bill = bike.returnVehicle(customer_obj.returnVehicle("bike"), "bike")
            customer_obj.rentalBasis_b, customer_obj.rentalTime_b, customer_obj.bikes = 0, 0, 0
            main_menu = True
        elif choice == 5:
            main_menu = True
        elif choice == 6:
            break
        else:
            print("Please enter a number between 1-6")

    elif choice.lower() == "b":
        print("""
        *********** CAR Menu **************
        1. Display available cars
        2. Request a car on hourly basis $10
        3. Request a car on daily basis $192
        4. Return a car
        5. Main menu
        6. Exit
        ************************************
        """)
        choice = input("Enter choice")

        try:
            choice = int(choice)
        except ValueError:
            print("Please enter a valid number")
            continue

        if choice == 1:
            car.displayStock()
        elif choice == 2:
            customer_obj.rentalTime_c = car.rentHourly(customer_obj.requestVehicle("car"))
            customer_obj.rentalBasis_c = 1
            main_menu = True
        elif choice == 3:
            customer_obj.rentalTime_c = car.rentDaily(customer_obj.requestVehicle("car"))
            customer_obj.rentalBasis_c = 2
            main_menu = True
        elif choice == 4:
            customer_obj.bill = car.returnVehicle(customer_obj.returnVehicle("car"), "car")
            customer_obj.rentalBasis_c, customer_obj.rentalTime_c, customer_obj.cars = 0, 0, 0
            main_menu = True
        elif choice == 5:
            main_menu = True
        elif choice == 6:
            break
        else:
            print("Please enter a number between 1-6")

    elif choice.lower() == "q":
        break

    else:
        print("Please enter a valid input (A-B-Q)")

print("Thank you...")
