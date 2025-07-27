a = "a"
b = "b"
c = "c"
d = "d"
e = "e"
f = "f"
g = "g"
h = "h"
i = "i"
game1 = [a,b,c]
game2 = [d,e,f]
game3 = [g,h,i]
print(game1)
print(game2)
print(game3)

t = False
x = 0
while x<9 :
    x = x+1
    player1 = input("player 1 choose from a-i : ")
    if player1 == "a" :
        a = "x" 
    elif player1 == "b":
        b = "x"
    elif player1 == "c":
        c = "x"
    elif player1 == "d":
        d = "x"
    elif player1 == "e":
        e = "x"
    elif player1 == "f":
        f = "x"
    elif player1 == "g":
        g = "x"
    elif player1 == "h":
        h = "x"
    elif player1 == "i":
        i = "x"
    
    game1 = [a,b,c]
    game2 = [d,e,f]
    game3 = [g,h,i]
    print(game1)
    print(game2)
    print(game3)

    if ((a == b == c) or 
        (d == e == f) or 
        (g == h == i) or 
        (a == d == g) or 
        (b == e == h) or 
        (c == f == i) or 
        (a == e == i) or 
        (c == e == g)):
        print("done!!!")
        t = True
        break

    player2 = input("player 2 choose from a-i : ")
    if player2 == "a" :
        a = "o" 
    elif player2 == "b":
        b = "o"
    elif player2 == "c":
        c = "o"
    elif player2 == "d":
        d = "o"
    elif player2 == "e":
        e = "o"
    elif player2 == "f":
        f = "o"
    elif player2 == "g":
        g = "o"
    elif player2 == "h":
        h = "o"
    elif player2 == "i":
        i = "o"
    game1 = [a,b,c]
    game2 = [d,e,f]
    game3 = [g,h,i]
    print(game1)
    print(game2)
    print(game3)

    if ((a == b == c) or 
        (d == e == f) or 
        (g == h == i) or 
        (a == d == g) or 
        (b == e == h) or 
        (c == f == i) or 
        (a == e == i) or 
        (c == e == g)):
        print("done!!!")
        t = True
        break
if t == False :
    print("the game is a draw")    