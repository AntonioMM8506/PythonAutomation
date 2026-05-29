print("Iterating over a string:")
my_string = "Ishtar"
for letter in my_string:
    print(letter)

print("\nList of numbers:")
my_list = [1, 2, 3, 4, 5]
for number in my_list:
    print(number)

print("\nTuple of numbers:")
my_tuple = (1, 2, 3, 4, 5)
for number in my_tuple:
    print(number)

print("\nDictionary of people:")
my_dict = {"name": "Ishtar", "age": 1000, "city": "Uruk"}
for key in my_dict:
    print(key)
for value in my_dict.values():
    print(value)
for key, value in my_dict.items():
    print(key, value)
for key in my_dict:
    print(key, my_dict[key])

print("\nRange of numbers:")
for i in range(5):
    print(i)