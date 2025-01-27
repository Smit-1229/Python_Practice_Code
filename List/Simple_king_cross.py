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

while status :
    user_input_guess = input("Enter Your Choice : ")
    coin = random.choice(game_list)
    
    print("User Choice : ",user_input_guess.capitalize())
    print("Coin Drop : ",coin)
    if user_input_guess.capitalize() == coin :
        print("You Won The Round")
      


    elif user_input_guess.capitalize() != coin and user_input_guess.capitalize() == "King" or user_input_guess.capitalize() == "Cross":
        print(("You Loss The Round"))
       
    else:
        print("Invalid Input")
    choice = input("Enter 'Y' for continue and 'n' for stop : " )
    if choice == 'n' or choice == "no":
        break

