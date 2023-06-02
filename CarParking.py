class ParkingLot:
    def __init__(self, small, medium, big):
        self.small_slots = small
        self.medium_slots = medium
        self.big_slots = big
        self.cars = []

    def add_car(self, registration_number, car_type):
        if self.is_slot_available(car_type):
            self.cars.append({"registration_number": registration_number,"car_type": car_type})
            self.update_availability(car_type)
            return True
        else:
            return False

    def remove_car(self, registration_number):
        for car in self.cars:
            if car["registration_number"] == registration_number:
                self.cars.remove(car)
                self.update_availability(car["car_type"])
                return True
        return False

    def get_car_details(self, registration_number):
        for car in self.cars:
            if car["registration_number"] == registration_number:
                return car
        return None

    def get_available_slots(self):
        #print(self.cars)
        return {
            "small": self.small_slots - len([car for car in self.cars if car["car_type"] == "small"]),
            "medium": self.medium_slots - len([car for car in self.cars if car["car_type"] == "medium"]),
            "big": self.big_slots - len([car for car in self.cars if car["car_type"] == "big"])
        }

    def get_occupied_slots(self):
        return {
            "small": len([car for car in self.cars if car["car_type"] == "small"]),
            "medium": len([car for car in self.cars if car["car_type"] == "medium"]),
            "big": len([car for car in self.cars if car["car_type"] == "big"])
        }

    def get_parked_cars(self):
        return self.cars

    def get_total_revenue(self):
        total_revenue = 0
        for car in self.cars:
            total_revenue += self.get_parking_fee(car["car_type"])
        return total_revenue

    def is_slot_available(self, car_type):
        return self.get_available_slots()[car_type] > 0

    def update_availability(self, car_type):
        self.get_available_slots()[car_type] -= 1

    def get_parking_fee(self, car_type):
        if car_type == "small":
            return 100
        elif car_type == "medium":
            return 200
        else:
            return 300


parking_lot = ParkingLot(small=10, medium=5, big=3)  #fixed slots for each car type

while True:
    
    
    print("****Parking Lot Design Test****")
    print("1.Add Car\n2.Remove Car\n3.Get Car Details\n4.Number of Available Parking Slots")
    print("5.Number of Occupied Parking Slots\n6.List of Parked Cars\n7.Total Revenue\n")
    option = int(input("Choose Your Option\n"))
    
    match option:
        
        case 1:
            registration_number=input("Provide Car Number (Example:AP-39-HH-1234)\n")
            op=int(input("Car Type\n Type 1 for small \n Type 2 for medium \n Type 3 for big\n"))
            car_type=None
            if op==1:
                car_type="small"
            if op==2:
                car_type="medium"
            if op==3:
                car_type="big"
            print(registration_number,car_type)
            flag=parking_lot.add_car(registration_number,car_type)
            if flag:
                print("Car Added Successfully")
            else:
                print("No Parking Slots for",car_type,"car type")

        case 2:
            registration_number = input("Provide Car Number (Example:AP-39-HH-1234)\n")
            parking_lot.remove_car(registration_number)
            print("Car Removed Successfully")

        case 3:
            print("****Car Details****\n")
            parked_cars = parking_lot.get_parked_cars()
            print(parked_cars)

        case 4:
            print("****Number of Available Parking Slots****\n")
            available_slots = parking_lot.get_available_slots()
            print(available_slots)

        case 5:
            print("****Number of Occupied Parking Slots****\n")
            occupied_slots = parking_lot.get_occupied_slots()
            print(occupied_slots)

        case 6:
            print("****List of Parked Cars****\n")
            parked_cars = parking_lot.get_parked_cars()
            print(parked_cars)

        case 7:
            total_revenue = parking_lot.get_total_revenue()
            print("Total Revenue=",total_revenue,"RS\-")

    choice=input("\nType NO to stop the process otherwise YES to continue\n")
    if choice=="NO":
        break
    
