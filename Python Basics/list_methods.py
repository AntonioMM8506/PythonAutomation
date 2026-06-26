cars = ["bmw", "honda", "audi"]

length = len(cars)
print(length)

cars.append("Benz")
print(cars)

cars.insert(1, "Jeep")
print(cars)

x = cars.index("honda")
print(x)

# returns an output
y = cars.pop()
print(y)
print(cars)

# it does not return an output
cars.remove("Jeep")
print(cars)

# returns an output withput altering the original array
slicing = cars[0:2]
print(slicing)

# Takes from the first index upto the end
slicing = cars[1:]
print(slicing)

# callback might not be supported, so doing print(cars.sort()) is not possible
cars.sort()
print(cars)
