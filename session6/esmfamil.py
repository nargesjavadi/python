a = int(input("how many players do you have ?"))
i = 0
game = ["first name" , "last name" , "color" , "fruit" , "animal" , "city" , "country"]
print(game)
while i < a :
    print("player" , i+1, ":") 
    j = 0
    while j < 6 :
        game [j] = input()
        j = j+1
    print(game)    
    i = i+1    