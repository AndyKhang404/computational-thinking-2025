try:
    a = float(input("Input number a:"))
    b = float(input("Input number b:"))
    print(f"{a}/{b} = {a/b}")
except ZeroDivisionError:
    print("Cannot divide by zero!!!")