class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    
    # Method to display the vehicle information
    def display_info(self):
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

# Main application
def main():
    print("Please enter the details for your car:")
    
    vehicle_type = "car"
    
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    
    while True:
        doors = input("Enter number of doors (2 or 4): ")
        if doors in ["2", "4"]:
            break
        print("Please enter either 2 or 4 for the number of doors.")
    
    while True:
        roof = input("Enter type of roof (solid or sun roof): ")
        if roof.lower() in ["solid", "sun roof"]:
            break
        print("Please enter either 'solid' or 'sun roof' for the roof type.")
    
    car = Automobile(vehicle_type, year, make, model, doors, roof)
    
    print("\nHere's your car information:")
    car.display_info()
    
if __name__ == "__main__":
    main()