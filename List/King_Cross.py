import random

menu = """                            
                            SOY Money Game
                        Choose One The Following
                                 King 
                                 Cross
                ****Double Your Money By Just Guessing**** 
                    
                                
                                """
game_list = ["King", "Cross"]
print(menu)
status = True
amount_input = 0
amount_exit = 0
while status :
    user_input_guess = input("Enter Your Choice : ")
    coin = random.choice(game_list)
    money = int(input("Enter Amount You Want To Input In Game:"))
    amount_input+=money
    print("User Choice : ",user_input_guess.capitalize())
    print("Coin Drop : ",coin)
    if user_input_guess.capitalize() == coin :
        print("You Won The Round")
        print(f"You Won {money*2}")
        amount_exit = (money*2)+amount_exit


    elif user_input_guess.capitalize() != coin and user_input_guess.capitalize() == "King" or user_input_guess.capitalize() == "Cross":
        print(("You Loss The Round"))
        print(f"You Won {money*0}")
    else:
        print("Invalid Input")
    choice = input("Enter 'Y' for continue and 'n' for stop : " )
    if choice == 'n' or choice == "no":
        break

print(f"Amount You Entered : {amount_input}")

print(f"Amount You Get : {amount_exit}")
if amount_input < amount_exit:
    print("profit : ",amount_exit-amount_input)
elif amount_input > amount_exit:
    print("loss : ", amount_input-amount_exit )
else: 
    print("No Profit No Loss")