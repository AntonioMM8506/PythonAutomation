# Like lists but they are unmutable (cannot be changed after creation)
# They are defined with parentheses () instead of square brackets
my_list = [1, 2, 3, 4, 5]
print(my_list)

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

print("tuple methods:")
print(my_tuple[0]) 
print(my_tuple[1:4])
print(my_tuple[-1])
print(my_tuple[::2])  # Slicing with a step
print(my_tuple[::-1])  # Reversing the tuple
print(my_tuple[1:])
print(len(my_tuple))
print(type(my_tuple))
print(my_tuple + (6, 7, 8))  # Concatenation of tuples
print(my_tuple * 2)  # Repetition of tuples
print(3 in my_tuple)  # Check if an element is in the tuple
print(my_tuple.count(2))  # Count the number of occurrences of an element
print(my_tuple.index(4))  # Get the index of the first occurrence of an element


my_tuple[0] = 10  # This will raise an error because tuples are unmutable
print(my_tuple)