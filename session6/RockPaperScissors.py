User1 = input("User 1 = ")
User2 = input("User 2 = ")

Winer = True

while Winer == True :
    # Winer = False
    User1Action = input("User 1 choose from rock paper scissors : ")
    User2Action = input("User 2 choose from rock paper scissors : ")

    if User1Action == "rock" and User2Action == "rock" :
        # Winer == True
        print("Similar choices ! please try again")
    elif User1Action == "paper" and User2Action == "paper" :
        # Winer == True 
        print("Similar choices ! please try again")
    elif User1Action == "scissors" and User2Action == "scissors" :
        # Winer == True  
        print("Similar choices ! please try again")
    elif User1Action == "rock" and User2Action == "paper" :
        print(User2 , "win!!")
        Winer == False
    elif User1Action == "rock" and User2Action == "scissors" :
        print(User1 , "win!!")
        Winer == False
    elif User1Action == "paper" and User2Action == "rock" :
        print(User1 , "win!!")
        Winer == False
    elif User1Action == "paper" and User2Action == "scissors" :
        print(User2 , "win!!")
        Winer == False
    elif User1Action == "scissors" and User2Action == "rock" :
        print(User2 , "win!!")
        Winer == False
    elif User1Action == "scissors" and User2Action == "paper" :
        print(User1 , "win!!")
        Winer == False 
    else :
        print("wrong choise")
