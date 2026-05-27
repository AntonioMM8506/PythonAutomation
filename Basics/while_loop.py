x = 0
while x < 10:
    x += 1
    if x == 8:
        print("x is 8, breaking the loop")
        break
    print(f"value of x: {x}")
    print("-"*20)
else:
    print("Loop completed without break")


y = 0
while y < 10:
    y += 1
    if y == 8:
        print("y is 8, continuing the loop")
        continue
    print(f"value of y: {y}")
    print("-"*20)
else:
    print("Loop completed without continue")


l = []
num = 0
while num < 10:
    l.append(num)
    num += 1
    print(f"value of num: {num}")
print(l)