class Car(object):
    wheels = 4

    # init method is a special method in Python classes, it is called when an instance of the class is created.
    # self is a reference to the current instance of the class, it is used to access variables that belong to the class.
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

    def drive(self):
        print(f"The {self.make} {self.model} is driving.")
    
    def stop(self):
        print(f"The {self.make} {self.model} has stopped.")
        

c1 = Car("BMW", "X5", 2020)
c2 = Car("Audi", "Q7", 2021)

print("Car 1:")
c1.display_info()  # Output: 2020 BMW X5
print(c1.wheels)  # Output: 4
print("Car 2:")
c2.display_info()  # Output: 2021 Audi Q7

c1.year = 2022
print("\nUpdated Car 1:")
c1.display_info()  # Output: 2022 BMW X5

