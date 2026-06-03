import car_class

# Inheritance: BMW is a subclass of Car, inheriting its properties and methods
# super() is used to call the __init__ method of the parent class (Car) to initialize the make, model, and year attributes.
# override the drive and stop methods to provide specific behavior for BMW cars.
class BMW(car_class.Car):
    def __init__(self, model, year):
        super().__init__("BMW", model, year)

    def drive(self):
        print(f"The BMW {self.model} is driving smoothly.")

    def stop(self):
        print(f"The BMW {self.model} has stopped gracefully.")

print("\nBMW Car:")
b1 = BMW("X5", 2020)
b1.display_info()  # Output: 2020 BMW X5
b1.drive()  # Output: The BMW X5 is driving smoothly.
b1.stop()  # Output: The BMW X5 has stopped gracefully.