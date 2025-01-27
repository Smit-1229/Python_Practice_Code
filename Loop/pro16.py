#accept name until user say no

status = True

while status :
    name =input("Enter Your name : ")
    choice = input("do you want to continue press 'y' for yes and 'n' for no :").lower()
    if choice == "y" or "yes":
        status = True
    else: 
        status = False
