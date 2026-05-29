# *args allows you to pass a variable number of arguments to a function.
def sum_nums(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_nums(1, 2, 3))  # Output: 6
print(sum_nums(10, 20, 30, 40))  # Output: 100