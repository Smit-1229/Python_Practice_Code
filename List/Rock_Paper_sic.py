import random

menu = """                       Menu
                Choose Any one the following 
                        Rock
                        Paper
                        Scissor 
"""
print(menu)
round = 1
Computer_won = 0
user_won = 0
tie = 0
game_list = ["Rock","Paper","Scissor"]
status = True
while status :
    print("Round : ",round)
    user_innput = input("Enter Your Choice : ").capitalize()
    computer_input = random.choice(game_list).capitalize()
    print("User Choice : ",user_innput)
    print("Computer Choice : ",computer_input)
    if user_innput == "Paper" and computer_input == "Scissor" :
        print(" Computer Won The Round ")
        Computer_won+=1

    elif user_innput == "Paper" and computer_input == "Rock" :
        print(" User Won The Round ")
        user_won+=1
 
    elif user_innput == "Rock" and computer_input == "Scissor" :
        print(" User Won The Round ")  
        user_won+=1        

    elif user_innput == "Rock" and computer_input == "Paper" :
        print(" Computer Won The Round ")
        Computer_won+=1

    elif user_innput == "Scissor" and computer_input == "Paper" :
        print(" User Won The Round ")
        user_won+=1

    elif user_innput == "Scissor" and computer_input == "Rock" :
        print(" Computer Won The Round ")
        Computer_won+=1

    else :
        print("The Round Has Been Tie")
        tie+=1

    round+=1
    print("Computer Won : ",Computer_won)
    print("User Won : ",user_won)
    print("Tie : ",tie)

    choice = input("Do You Wnat To Continue Press 'y' for Yes and 'n' for no : ")
    if choice == "no" or choice == "n":
        break
