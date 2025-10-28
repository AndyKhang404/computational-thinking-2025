n = int(input("Input a number: "))
match n:
    case int(x) if x > 0:
        print("Số dương")
    case int(x) if x < 0:
        print("Số âm")
    case int(x) if x == 0:
        print("Số không")
    case _:
        pass