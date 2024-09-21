# Calculator with menu to add, subtract, multiply, divide
class add:
    def __init__(add, fn1, fn2):
        add.fn1 = fn1
        add.fn2 = fn2
        result = fn1 + fn2
        print("This is the sum: ", result)


class subtract:
    def __init__(sub, a, b):
        sub.a = a
        sub.b = b
        result = a - b
        print("After subtracting the answer is: ", result)


class multiply:
    def __init__(mul, c, d):
        mul.c = c
        mul.d = d
        result = 0
        for x in range(d):
            result += c
        print("After multiplying the answer is: ", result)


class divide:
    def __init__(div, e, f):
        div.e = e
        div.f = f
        result = e / f
        print("After dividing the answer is: ", result)


x = ""  # initializer
while x != "end":
    x = input("Choose operand: add; subract; multiply; divide; end     ")
    if x == "add":
        a = int(input("First Number "))
        b = int(input("Second Number "))
        add(a, b)
    elif x == "subtract":
        a = int(input("First Number "))
        b = int(input("Second Number "))
        subtract(a, b)
    elif x == "multiply":
        a = int(input("First Number "))
        b = int(input("Second Number "))
        multiply(a, b)
    elif x == "divide":
        a = int(input("First Number "))
        b = int(input("Second Number "))
        divide(a, b)
    elif x == "end":
        print("\nGoodBye")
    else:
        print("Invalid Input \n Try Again")