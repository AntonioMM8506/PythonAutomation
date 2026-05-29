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

print("\nRange of numbers with start and end:")
for i in range(2, 7):
    print(i)

print("\nRange of numbers with step:")
for i in range(0, 10, 2):
    print(i)

print("\nRange of numbers in reverse:")
for i in range(10, 0, -1):
    print(i)

print("\nRange of numbers with negative step:")
for i in range(10, 0, -2):
    print(i)

print("\nIndexing in a string:")
my_string = "Ishtar"
for i in range(len(my_string)):
    print(my_string[i])

print("\nEnumerate in a list:")
my_list = ['a', 'b', 'c', 'd', 'e']
for index, value in enumerate(my_list):
    print(index, value)

print("\nIterating over a list of lists:")
my_list_of_lists = [[1, 2], [3, 4], [5, 6]]
for sublist in my_list_of_lists:
    for item in sublist:
        print(item)

print("\nIterating over a list of dictionaries:")
my_list_of_dicts = [{"name": "Ishtar", "age": 1000}, {"name": "Gilgamesh", "age": 2500}]
for person in my_list_of_dicts:
    for key, value in person.items():
        print(key, value)

print("\nIterating over a string with enumerate:")
my_string = "Ishtar"
for index, letter in enumerate(my_string):
    print(index, letter)

print("\nIterating over a list with enumerate:")
my_list = ['a', 'b', 'c', 'd', 'e']
for index, value in enumerate(my_list):
    print(index, value) 

print("\nIterating over a list of lists with enumerate:")
my_list_of_lists = [[1, 2], [3, 4], [5, 6]]
for index, sublist in enumerate(my_list_of_lists):
    print("Sublist index:", index)
    for item in sublist:
        print(item) 

print("\nIterating over a list of dictionaries with enumerate:")
my_list_of_dicts = [{"name": "Ishtar", "age": 1000}, {"name": "Gilgamesh", "age": 2500}]
for index, person in enumerate(my_list_of_dicts):    
    print("Person index:", index)
    for key, value in person.items():
        print(key, value) 

print("\nIterating over a string with enumerate and start index:")
my_string = "Ishtar"
for index, letter in enumerate(my_string, start=1):
    print(index, letter)

print("\nIterating over a list with enumerate and start index:")
my_list = ['a', 'b', 'c', 'd', 'e']
for index, value in enumerate(my_list, start=1):
    print(index, value)

print("\nUsing range(len(my_list)):")
for i in range(len(my_list)):
    print(i, my_list[i])