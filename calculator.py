def addition():
    user_num = float(input("Enter the number: "))
    ans = 0
    ans += user_num
    while user_num != 0:
        user_num = float(input("Enter the number you want to add, or zero to see the result: "))
        ans += user_num
    return ans

def subtraction():
    user_num = float(input("Enter the number: "))
    ans = 0
    ans += user_num
    while user_num != 0:
        user_num = float(input("Enter the number you want to subtract, or zero to see the result: "))
        ans -= user_num
    return ans

def multiplication():
    user_num = float(input("Enter the number: "))
    ans = 0
    ans += user_num
    while user_num != 0:
        user_num = float(input("Enter the number you want to multiply it by, or zero to see the result: "))
        if user_num == 0:
            break
        else:
            ans *= user_num
    return ans

def division():
    user_num = float(input("Enter the number: "))
    ans = 0
    ans += user_num
    while user_num != 0:
        user_num = float(input("Enter the number you want to divide it by, or zero to see the result: "))
        if user_num == 0:
            break
        else:
            ans /= user_num
    return ans

while True:
    options = ["a", "s", "m", "d", "q"]
    print("Simple calculator.")
    print('Enter "a" for addition')
    print('Enter "s" for substraction')
    print('Enter "m" for multiplication')
    print('Enter "d" for division')
    print('Enter "q" to quit')
    calculate = str(input())
    if calculate != "q":
        if calculate == "a":
            print(addition())
        elif calculate == "s":
            print(subtraction())
        elif calculate == "m":
            print(multiplication())
        elif calculate == "d":
            print(division())
        elif calculate not in options:
            print(calculate + " is not one of the options. Please try again.")
            continue
    else:
        break
