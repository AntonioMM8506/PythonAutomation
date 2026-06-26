car = {
    "make" : "bmw",
    "model": "5501",
    "year": 2011
}


cars = {
    "audi": {"model": "a6", "year": 2010, "color": "white"},
    "toyota": {"model": "camry", "year": 2009, "color": "silver"},
    "honda": {"model": "accord", "year": 2008, "color": "blue"},
    "benz": {"model": "c300", "year": 2012, "color": "black"}
}

print("simple dictionary")
print(car.keys())
print(car.values())
print(car.items())

print("\nnested dictionary")
print(cars.keys())
print(cars.values())
print(cars.items())


car_copy = car.copy()
print("\ncar copy")
print(car_copy)


car_copy.pop("model")
print("\ncar copy after pop")
print(car_copy)


car.clear()
print("\ncar after clear")
print(car)


cars["audi"].clear()
print("\naudi after clear")
print(cars["audi"])
print("\ncars after clear")
print(cars)
