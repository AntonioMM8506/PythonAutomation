a = 10

def test_method(a):
    a = 5
    print("Inside the method, a =", a)

test_method(10)  # Output: Inside the method, a = 5
print("Outside the method, a =", a)  # Output: Outside the method, a = 10


# global keyword allows you to modify a variable outside of the current scope.
print("\nUsing global keyword:")
def test_method_with_global():
    global a
    a = 5
    print("Inside the method with global, a =", a)

test_method_with_global()
print("Outside the method with global, a =", a)  # Output: Outside the method with global, a = 5