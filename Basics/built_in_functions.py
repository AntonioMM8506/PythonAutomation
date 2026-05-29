def largest_number(*args):
    if not args:
        return None  # Return None if no arguments are provided
    print(max(args))  
    largest = max(args)  
    return largest  

def smallest_number(*args):
    if not args:
        return None  
    print(min(args)) 
    smallest = min(args)  
    return smallest  

largest_number(3, 1, 4, 1, 5, 9)  # Output: 9
smallest_number(3, 1, 4, 1, 5, 9)  # Output: 1

def average(*args):
    if not args:
        return None  
    total = sum(args)  
    count = len(args)  
    average_value = total / count  
    print(average_value)  
    return average_value  

def abs_function(num):
    absolute_value = abs(num)  
    print(absolute_value)  
    return absolute_value 


average(3, 1, 4, 1, 5, 9)  # Output: 3.8333333333333335
abs_function(-10)  # Output: 10

def round_number(num, ndigits=0):
    rounded_value = round(num, ndigits)  
    print(rounded_value)  
    return rounded_value

def pow_function(base, exp):
    power_value = pow(base, exp)  
    print(power_value)  
    return power_value

def divmod_function(a, b):
    quotient, remainder = divmod(a, b)  
    print(f"Quotient: {quotient}, Remainder: {remainder}")  
    return quotient, remainder

round_number(3.14159, 2)  # Output: 3.14
pow_function(2, 3)  # Output: 8
divmod_function(10, 3)  # Output: Quotient: 3, Remainder: 1

def sorted_numbers(*args):
    sorted_list = sorted(args)  
    print(sorted_list)  
    return sorted_list

def reversed_string(s):
    reversed_str = s[::-1]  
    print(reversed_str)  
    return reversed_str

sorted_numbers(3, 1, 4, 1, 5, 9)  # Output: [1, 1, 3, 4, 5, 9]
reversed_string("Hello, World!")  # Output: !dlroW ,olleH

def enumerate_list(lst):
    enumerated_list = list(enumerate(lst))  
    print(enumerated_list)  
    return enumerated_list

enumerate_list(['a', 'b', 'c'])  # Output: [(0, 'a'), (1, 'b'), (2, 'c')]

print(type(largest_number))  # Output: <class 'function'>
print(type(9))  # Output: <class 'int'>
print(type(3.14))  # Output: <class 'float'>
print(type("Hello"))  # Output: <class 'str'>
print(type([1, 2, 3]))  # Output: <class 'list'>
print(type((1, 2, 3)))  # Output: <class 'tuple'>
print(type({'a': 1, 'b': 2}))  # Output: <class 'dict'>    
print(type({1, 2, 3}))  # Output: <class 'set'>
print(type(None))  # Output: <class 'NoneType'>
print(type(True))  # Output: <class 'bool'>
