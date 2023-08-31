import datetime
#%%parent class


class vehicleRent:
    def __init__(self,stock):
        self.stock = stock
        self.now = 0

    def displayStock(self):
        """
            Display Stock
        """
        print("{} vehicle available to rent".format(self.stock))
        return self.stock

    def rentHourly(self, n):
        """
        Rent Hourly
        """
        if n <= 0:
            print("Number should be positive")
            return None
        elif n > self.stock:
            print("Sorry, only {} vehicle(s) available to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented {} vehicle(s) hourly at {} hour(s).".format(n, self.now.hour))
            self.stock -= n  # Stoktan düşürülüyor
            return self.now

    def rentDaily(self, n):
        """
        Rent Daily
        """
        if n <= 0:
            print("Number should be positive")
            return None
        elif n > self.stock:
            print("Sorry, only {} vehicle(s) available to rent".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented {} vehicle(s) daily at {} hour(s).".format(n, self.now.hour))
            self.stock -= n  # Stoktan düşürülüyor
            return self.now

    def returnVehicle(self,request,brand):
        """
            return a bill
        """

        car_h_price = 10
        car_d_price = car_h_price*8/10*24
        bike_h_price = 2
        bike_d_price = bike_h_price*7/10*24

        rentalTime,rentalBasis,numOfVehicle = request
        bill = 0
        if brand == "car":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
            
                if rentalBasis == 1:#hourly
                    bill = rentalPeriod.seconds/3600*car_h_price*numOfVehicle
                elif rentalBasis == 2:#daily
                    bill = rentalPeriod.seconds/(3600*24)*car_d_price*numOfVehicle
                if (2 <= numOfVehicle):
                    print("You have extra 20%  discount")
                    bill = bill*0.8

                print("thank you for returning your vehicle")
                print("Price: ${}".format(bill))
                return bill
        if brand == "bike":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime
            
                if rentalBasis == 1:#hourly
                    bill = rentalPeriod.seconds/3600*bike_h_price*numOfVehicle
                elif rentalBasis == 2:#daily
                    bill = rentalPeriod.seconds/(3600*24)*bike_d_price*numOfVehicle
                if (4 <= numOfVehicle):
                    print("You have extra 20%  discount")
                    bill = bill*0.8

                print("thank you for returning your vehicle")
                print("Price: ${}".format(bill))
                return bill
        else:
            print("you do not rent a vehicle")


#%%child class(car)

class carRent(vehicleRent):
    discount_rate = 15  # discount_rate'i buraya taşıyın
    def __init__(self,stock):
        super().__init__(stock)

    def discount(self,b):
        bill = b - (b * self.discount_rate)/100  # discount_rate'i burada kullanın
        return bill


#%%child class2(bike)

class bikeRent(vehicleRent):
    def __init__(self, stock):
        super().__init__(stock)

#%%customer

class customer:
    def __init__(self):
        self.cars = 0
        self.rentalBasis_c = 0
        self.rentalTime_c = 0

        self.bikes = 0
        self.rentalBasis_b = 0
        self.rentalTime_b = 0

    def requestVehicle(self, brand):
        if brand == "bike":
            bikes = input("How many bikes would you like to rent")
            try:
                bikes = int(bikes)
            except(ValueError):
                print("Please input number")
                return -1

            if bikes < 1:
                print("Number should be greater than zero")
                return -1
            else:
                self.bikes = bikes
            return self.bikes

        elif brand == "car":
            cars = input("How many car would you like to rent")  # Değiştir cars -> car
            try:
                cars = int(cars)
            except(ValueError):
                print("Please input number")
                return -1

            if cars < 1:
                print("Number should be greater than zero")
                return -1
            else:
                self.cars = cars  # Değiştir cars -> self.cars
            return self.cars

        else:
            print("Request vehicle error")

    def returnVehicle(self, brand):
        if brand == "car":
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c, self.rentalBasis_c, self.cars
            else:
                return (0, 0, 0)
        elif brand == "bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b, self.rentalBasis_b, self.bikes
            else:
                return (0, 0, 0)
        else:
            print("Return vehicle error")

        