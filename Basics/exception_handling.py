def exceptionHandling(a, b, c):
    try:
        d = (a + b)/c
        print(d)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Invalid input type. Please provide numbers.")
    else:
        print("The operation was successful.")
    finally:
        print("This block will always execute, regardless of exceptions.\n")

exceptionHandling(10, 20, 10)
exceptionHandling(10, 20, 0)
exceptionHandling(10, 20, "some string")
exceptionHandling(10, None, None)