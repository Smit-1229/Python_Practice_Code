sum = 0
flag = True
while flag:
    num = int(input("Enter Nummber : "))
    sum += num
    choice = input("Enter 'y' for continue & 'n' for stop: ").lower()
    if choice == "y":
        flag = True
    else :
        flag = False
