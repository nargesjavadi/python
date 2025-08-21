import random
squares = {"a1" : "⚪" , "a2" : "⚪" , "a3" : "⚪" , "a4" : "⚪" , "a5" : "⚪" ,"a6" : "⚪" , "a7" : "⚪" , "a8" : "⚪" , "a9" : "⚪" , "a10" : "⚪" ,
           "a11" : "⚪" , "a12" : "⚪" , "a13" : "⚪" , "a14" : "⚪" , "a15" : "⚪" , "a16" : "⚪" , "a17" : "⚪" , "a18" : "⚪" , "a19" : "⚪" , "a20" : "⚪" ,
           "a21" : "⚪" , "a22" : "⚪" , "a23" : "⚪" , "a24" : "⚪" , "a25" : "⚪" , "a26" : "⚪" , "a27" : "⚪" , "a28" : "⚪" , "a29" : "⚪" , "a30" : "⚪" , 
           "a31" : "⚪" , "a32" : "⚪" , "a33" : "⚪" , "a34" : "⚪" , "a35" : "⚪" , "a36" : "⚪" , "a37" : "⚪" , "a38" : "⚪" , "a39" : "⚪" , "a40" : "⚪" ,}
k = {"blue" : ["🔵","🔵","🔵","🔵"],
     "yellow" : ["🟡","🟡","🟡","🟡"],
     "green" : ["🟢","🟢","🟢","🟢"],
     "red" : ["🔴","🔴","🔴","🔴"]}
m = {"blue" : ["🔵","🔵","🔵","🔵"],
     "yellow" : ["🟡","🟡","🟡","🟡"],
     "green" : ["🟢","🟢","🟢","🟢"],
     "red" : ["🔴","🔴","🔴","🔴"]}
def print_squares():
    print("  ",m["yellow"][2],m["yellow"][3],"  ",squares["a19"]," ",squares["a20"]," ",squares["a21"],"  ",m["blue"][2],m["blue"][3],"  ")
    print("  ",m["yellow"][0],m["yellow"][1],"  ",squares["a18"], " ",k["blue"][0]," ",squares["a22"],"  ",m["blue"][0],m["blue"][1],"  ")
    print("           ",squares["a17"], " ",k["blue"][1]," ",squares["a23"])
    print("           ",squares["a16"], " ",k["blue"][2]," ",squares["a24"])
    print(squares["a11"],squares["a12"],squares["a13"],squares["a14"],squares["a15"]," ",k["blue"][3]," ",squares["a25"],squares["a26"],squares["a27"],squares["a28"],squares["a29"])
    print(squares["a10"],k["yellow"][0],k["yellow"][1],k["yellow"][2],k["yellow"][3],"      ",k["green"][0],k["green"][1],k["green"][2],k["green"][3],squares["a30"])
    print(squares["a9"],squares["a8"],squares["a7"],squares["a6"],squares["a5"]," ",k["red"][3]," ",squares["a35"],squares["a34"],squares["a37"],squares["a38"],squares["a39"])
    print("           ",squares["a4"], " ",k["red"][2]," ",squares["a36"])
    print("           ",squares["a3"], " ",k["red"][1]," ",squares["a37"])
    print("  ",m["red"][2],m["red"][3],"  ",squares["a2"], " ",k["red"][0]," ",squares["a38"],"  ",m["green"][2],m["green"][3],"  ")
    print("  ",m["red"][0],m["red"][1],"  ",squares["a1"]," ",squares["a40"]," ",squares["a39"],"  ",m["green"][0],m["green"][1],"  ")
print_squares()
def blue_turn(squares,k,m):
    a = [1,2,3,4,5,6]
    x = random.choice(a)
    print("blue dice : " , x)
    for key,value in list(squares.items()):
        if value == "🔵":
            key1 = int(key[1:3])
            squares[key] = "⚪"
            key2 = str(key1 + x)
            squares["a"+key2] = "🔵"
        else:
            if x == 6:
                m["blue"][0] = "⚪"
                squares["a21"] = "🔵"
                x = random.choice(a)
                key1 = 21
                print("blue dice : " , x)
                squares["a21"] = "⚪"
                key2 = str(key1 + x)
                squares["a"+key2] = "🔵"

def yellow_turn(squares,k,m):
    a = [1,2,3,4,5,6]
    x = random.choice(a)
    print("yellow dice : " , x)
    for key,value in list(squares.items()):
        if value == "🟡":
            key1 = int(key[1:3])
            squares[key] = "⚪"
            key2 = str(key1 + x)
            squares["a"+key2] = "🟡"
        else:
            if x == 6:
                m["yellow"][0] = "⚪"
                squares["a11"] = "🟡"
                x = random.choice(a)
                key1 = 11
                print("yellow dice : " , x)
                squares["a11"] = "⚪"
                key2 = str(key1 + x)
                squares["a"+key2] = "🟡"

def green_turn(squares,k,m):
    a = [1,2,3,4,5,6]
    x = random.choice(a)
    print("green dice : " , x)
    for key,value in list(squares.items()):
        if value == "🟢":
            key1 = int(key[1:3])
            squares[key] = "⚪"
            key2 = str(key1 + x)
            squares["a"+key2] = "🟢"
        else:
            if x == 6:
                m["green"][0] = "⚪"
                squares["a31"] = "🟢"
                x = random.choice(a)
                key1 = 31
                print("green dice : " , x)
                squares["a31"] = "⚪"
                key2 = str(key1 + x)
                squares["a"+key2] = "🟢"
    
def red_turn(squares,k,m):
    a = [1,2,3,4,5,6]
    x = random.choice(a)
    print("red dice : " , x)
    for key,value in list(squares.items()):
        if value == "🔴":
            key1 = int(key[1:3])
            squares[key] = "⚪"
            key2 = str(key1 + x)
            squares["a"+key2] = "🔴"
        else:
            if x == 6:
                m["red"][0] = "⚪"
                squares["a1"] = "🔴"
                x = random.choice(a)
                key1 = 1
                print("red dice : " , x)
                squares["a1"] = "⚪"
                key2 = str(key1 + x)
                squares["a"+key2] = "🔴"
i =0
while i<12:
    print("")
    red_turn(squares,k,m)
    print_squares()
    yellow_turn(squares,k,m)
    print_squares()
    blue_turn(squares,k,m)
    print_squares()
    green_turn(squares,k,m)
    print_squares()
    i = i+1