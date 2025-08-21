import random
squares = { "a1" : "WRa" , "a2" : "WPa" , "a3" : "   " , "a4" : "   " , "a5" : "   " , "a6" : "   " , "a7" : "BPa" , "a8" : "BRa" ,
            "b1" : "WNb" , "b2" : "WPb" , "b3" : "   " , "b4" : "   " , "b5" : "   " , "b6" : "   " , "b7" : "BPb" , "b8" : "BNb" ,
            "c1" : "WBc" , "c2" : "WPc" , "c3" : "   " , "c4" : "   " , "c5" : "   " , "c6" : "   " , "c7" : "BPc" , "c8" : "BBc" ,
            "d1" : "WQ " , "d2" : "WPd" , "d3" : "   " , "d4" : "   " , "d5" : "   " , "d6" : "   " , "d7" : "BPd" , "d8" : "BQ " ,
            "e1" : "WK " , "e2" : "WPe" , "e3" : "   " , "e4" : "   " , "e5" : "   " , "e6" : "   " , "e7" : "BPe" , "e8" : "BK " ,
            "f1" : "WBf" , "f2" : "WPf" , "f3" : "   " , "f4" : "   " , "f5" : "   " , "f6" : "   " , "f7" : "BPf" , "f8" : "BBf" ,
            "g1" : "WNg" , "g2" : "WPg" , "g3" : "   " , "g4" : "   " , "g5" : "   " , "g6" : "   " , "g7" : "BPg" , "g8" : "BNg" ,
            "h1" : "WRh" , "h2" : "WPh" , "h3" : "   " , "h4" : "   " , "h5" : "   " , "h6" : "   " , "h7" : "BPh" , "h8" : "BRh"
}

def print_squares(squares):
    print("     a     b     c     d     e     f     g     h")
    print("  =================================================")
    print("8 ‖" , squares["a8"] ,"|" , squares["b8"] ,"|" , squares["c8"] ,"|" , squares["d8"] ,"|" , squares["e8"] ,"|" , squares["f8"] ,"|" , squares["g8"] ,"|" , squares["h8"] ,"‖ 8")
    print("   -----+-----+-----+-----+-----+-----+-----+-----")
    print("7 ‖" , squares["a7"] ,"|" , squares["b7"] ,"|" , squares["c7"] ,"|" , squares["d7"] ,"|" , squares["e7"] ,"|" , squares["f7"] ,"|" , squares["g7"] ,"|" , squares["h7"] ,"‖ 7")
    print("   -----+-----+-----+-----+-----+-----+-----+-----")
    print("6 ‖" , squares["a6"] ,"|" , squares["b6"] ,"|" , squares["c6"] ,"|" , squares["d6"] ,"|" , squares["e6"] ,"|" , squares["f6"] ,"|" , squares["g6"] ,"|" , squares["h6"] ,"‖ 6")
    print("   -----+-----+-----+-----+-----+-----+-----+-----")
    print("5 ‖" , squares["a5"] ,"|" , squares["b5"] ,"|" , squares["c5"] ,"|" , squares["d5"] ,"|" , squares["e5"] ,"|" , squares["f5"] ,"|" , squares["g5"] ,"|" , squares["h5"] ,"‖ 5")
    print("   -----+-----+-----+-----+-----+-----+-----+-----")
    print("4 ‖" , squares["a4"] ,"|" , squares["b4"] ,"|" , squares["c4"] ,"|" , squares["d4"] ,"|" , squares["e4"] ,"|" , squares["f4"] ,"|" , squares["g4"] ,"|" , squares["h4"] ,"‖ 4")
    print("   -----+-----+-----+-----+-----+-----+-----+-----")
    print("3 ‖" , squares["a3"] ,"|" , squares["b3"] ,"|" , squares["c3"] ,"|" , squares["d3"] ,"|" , squares["e3"] ,"|" , squares["f3"] ,"|" , squares["g3"] ,"|" , squares["h3"] ,"‖ 3")
    print("   -----+-----+-----+-----+-----+-----+-----+-----")
    print("2 ‖" , squares["a2"] ,"|" , squares["b2"] ,"|" , squares["c2"] ,"|" , squares["d2"] ,"|" , squares["e2"] ,"|" , squares["f2"] ,"|" , squares["g2"] ,"|" , squares["h2"] ,"‖ 2")
    print("   -----+-----+-----+-----+-----+-----+-----+-----")
    print("1 ‖" , squares["a1"] ,"|" , squares["b1"] ,"|" , squares["c1"] ,"|" , squares["d1"] ,"|" , squares["e1"] ,"|" , squares["f1"] ,"|" , squares["g1"] ,"|" , squares["h1"] ,"‖ 1")
    print("  =================================================")
    print("     a     b     c     d     e     f     g     h")

print_squares(squares)
def user_turn(a,b,squares):
    b1 = b[0]
    b2 = b[1]
    nlist = ["a","b","c","d","e","f","g","h"]
    p = 1
    for i in nlist:
        if b1 == i:
            b3 = p
            break
        else:
            p = p + 1
    a1 = a[0]+a[1]
    a2 = a[2]
    for key,value in squares.items():
            if value == a: 
                key1 = key
                key0 = key1[0]
                key2 = key1[1]
                key3 = int(key2)+1
                key4 = int(key2)-1
                key3 = str(key3)
                break
    q = 1
    for i in nlist:
        if key0 == i:
            key6 = q
            break
        else:
            q = q + 1        
    if a1 == "WP":
        c = nlist[b3-1]
        c2 = nlist[b3-2]
        for i in nlist:
            if a == "WP"+i:
                key4 = str(key4)
                if  squares[c+key3] != "   " :
                    squares[b] = a
                    squares[key1] = "   "
                elif squares[c2+key4] != "   ":
                    squares[b] = a
                    squares[key1] = "   "
                elif (b == i+"3" or b == i+"4") and squares[b] == "   " and key2 == "2" :
                    squares[b] = a
                    squares[key1] = "   "
                elif b == i+key3:
                    squares[b] = a
                    squares[key1] = "   "
                else:
                    print("illegal move")

    elif a1 == "WR":
        t = True
        if key2 == b2 :
            key2 = int(key2)+1 
            b3 = int(b3)
            x = nlist.index(key0)
            while key2 <= b3:
                for i in nlist[x:b3] :
                    if squares[i+b2] == "   " or squares[b] !="   ":
                        key2 = key2+1
                    else: 
                        t = False
                        break
                break
        if key0 == b1:
            i = int(key2)+1
            b2 = int(b2)
            while i <= b2:
                i = str(i)
                if squares[b1+i] == "   ":
                    i = int(i)
                    i = i+1
                else:
                    t = False
                    break
        if t == True:
            squares[b] = a
            squares[key1] = "   "
        else:
            print("illegal move")

    elif a1 == "WB":
        x = (nlist.index(key0))+1
        t = True
        j = int(key2)+1
        b2 = int(b2)
        key2 = int(key2)
        if b2 > key2:
            for i in nlist[x:b3]:
                while j<=b2:
                    if squares[i+str(j)] == "   " or squares[b] != "   ":
                       j = j+1
                       break
                    else:
                        t = False
                        break
                break
        elif key2>b2 :
            nlist.reverse()
            for i in nlist[x:b3]:
                while j>=b2:
                    if squares[i+str(j)] == "   " or squares[b] != "   ":
                       j = j-1
                       break
                    else:
                        t = False
                        break
                break
            nlist.reverse()
        else:
            print("illegal move")
        if t == True:
            squares[b] = a
            squares[key1] = "   "
        else:
            print("illegal move")

    elif a1 == "WQ":
        t = True
        if key2 == b2 :
            key2 = int(key2)+1 
            b3 = int(b3)
            x = nlist.index(key0)
            while key2 <= b3:
                for i in nlist[x:b3] :
                    if squares[i+b2] == "   " or squares[b] !="   ":
                        key2 = key2+1
                    else: 
                        t = False
                        break
                break
        if key0 == b1:
            i = int(key2)+1
            b2 = int(b2)
            while i <= b2:
                i = str(i)
                if squares[b1+i] == "   ":
                    i = int(i)
                    i = i+1
                else:
                    t = False
                    break

        x = (nlist.index(key0))+1
        j = int(key2)+1
        b2 = int(b2)
        key2 = int(key2)
        if b2 > key2:
            for i in nlist[x:b3]:
                while j<=b2:
                    if squares[i+str(j)] == "   " or squares[b] != "   ":
                       j = j+1
                       break
                    else:
                        t = False
                        break
                break
        elif key2>b2 :
            nlist.reverse()
            for i in nlist[x:b3]:
                while j>=b2:
                    if squares[i+str(j)] == "   " or squares[b] != "   ":
                       j = j-1
                       break
                    else:
                        t = False
                        break
                break
            nlist.reverse()
        else:
            print("illegal move")
        if t == True:
            squares[b] = a
            squares[key1] = "   "
        else:
            print("illegal move") 
    elif a1 == "WN":
        x = abs(b3-key6)  
        b2 = int(b2)
        key2 = int(key2)
        y = abs(b2 - key2)     
        if (x == 2 and y == 1) or (x == 1 and y == 2):
            squares[b] = a
            squares[key1] = "   "
        else:
            print("illegal move")
    elif a1 == "WK":
        b2 = int(b2)
        key2 = int(key2)
        if (b1 == key0 and (b2 == key2+1 or b2 == key2-1)) or (b2 == key2 and (b3 == key6-1 or b3 == key6+1)) or (b3 == key6-1 and (b2 == key2+1 or b2 == key2-1)) or (b2 == key2+1 and (b2 == key2+1 or b2 == key2-1)):
            squares[b] = a
            squares[key1] = "   "
        else:
            print("illegal move")

def bot_turn(squares):
    while True:
        value1 = []
        for value in squares.values():
            if value.startswith("B"):
                value1.append(value)
        a = random.choice(value1)
        b = random.choice(list(squares.keys()))
        b1 = b[0]
        b2 = b[1]
        nlist = ["a","b","c","d","e","f","g","h"]
        p = 1
        for i in nlist:
            if b1 == i:
                b3 = p
                break
            else:
                p = p + 1
        a1 = a[0]+a[1]
        a2 = a[2]
        for key,value in squares.items():
                if value == a: 
                    key1 = key
                    key0 = key1[0]
                    key2 = key1[1]
                    key3 = int(key2)+1
                    key4 = int(key2)-1
                    key3 = str(key3)
                    break
        q = 1
        for i in nlist:
            if key0 == i:
                key6 = q
                break
            else:
                q = q + 1        
        if a1 == "BP":
            c = nlist[b3-1]
            c2 = nlist[b3-2]
            for i in nlist:
                if a == "BP"+i:
                    key4 = str(key4)
                    if  squares[c+key3] != "   " :
                        squares[b] = a
                        squares[key1] = "   "
                    elif squares[c2+key4] != "   ":
                        squares[b] = a
                        squares[key1] = "   "
                    elif (b == i+"3" or b == i+"4") and squares[b] == "   " and key2 == "2" :
                        squares[b] = a
                        squares[key1] = "   "
                    elif b == i+key3:
                        squares[b] = a
                        squares[key1] = "   "
                    else:
                        continue

        elif a1 == "BR":
            t = True
            if key2 == b2 :
                key2 = int(key2)+1 
                b3 = int(b3)
                x = nlist.index(key0)
                while key2 <= b3:
                    for i in nlist[x:b3] :
                        if squares[i+b2] == "   " or squares[b] !="   ":
                            key2 = key2+1
                        else: 
                            t = False
                            break
                    break
            if key0 == b1:
                i = int(key2)+1
                b2 = int(b2)
                while i <= b2:
                    i = str(i)
                    if squares[b1+i] == "   ":
                        i = int(i)
                        i = i+1
                    else:
                        t = False
                        break
            if t == True:
                squares[b] = a
                squares[key1] = "   "
            else:
                continue

        elif a1 == "BB":
            x = (nlist.index(key0))+1
            t = True
            j = int(key2)+1
            b2 = int(b2)
            key2 = int(key2)
            if b2 > key2:
                for i in nlist[x:b3]:
                    while j<=b2:
                        if squares[i+str(j)] == "   " or squares[b] != "   ":
                           j = j+1
                           break
                        else:
                            t = False
                            break
                    break
            elif key2>b2 :
                nlist.reverse()
                for i in nlist[x:b3]:
                    while j>=b2:
                        if squares[i+str(j)] == "   " or squares[b] != "   ":
                           j = j-1
                           break
                        else:
                            t = False
                            break
                    break
                nlist.reverse()
            else:
                continue
            if t == True:
                squares[b] = a
                squares[key1] = "   "
            else:
                continue

        elif a1 == "BQ":
            t = True
            if key2 == b2 :
                key2 = int(key2)+1 
                b3 = int(b3)
                x = nlist.index(key0)
                while key2 <= b3:
                    for i in nlist[x:b3] :
                        if squares[i+b2] == "   " or squares[b] !="   ":
                            key2 = key2+1
                        else: 
                            t = False
                            break
                    break
            if key0 == b1:
                i = int(key2)+1
                b2 = int(b2)
                while i <= b2:
                    i = str(i)
                    if squares[b1+i] == "   ":
                        i = int(i)
                        i = i+1
                    else:
                        t = False
                        break
    
            x = (nlist.index(key0))+1
            j = int(key2)+1
            b2 = int(b2)
            key2 = int(key2)
            if b2 > key2:
                for i in nlist[x:b3]:
                    while j<=b2:
                        if squares[i+str(j)] == "   " or squares[b] != "   ":
                           j = j+1
                           break
                        else:
                            t = False
                            break
                    break
            elif key2>b2 :
                nlist.reverse()
                for i in nlist[x:b3]:
                    while j>=b2:
                        if squares[i+str(j)] == "   " or squares[b] != "   ":
                           j = j-1
                           break
                        else:
                            t = False
                            break
                    break
                nlist.reverse()
            else:
                continue
            if t == True:
                squares[b] = a
                squares[key1] = "   "
            else:
                continue 
        elif a1 == "BN":
            x = abs(b3-key6)  
            b2 = int(b2)
            key2 = int(key2)
            y = abs(b2 - key2)     
            if (x == 2 and y == 1) or (x == 1 and y == 2):
                squares[b] = a
                squares[key1] = "   "
            else:
                continue
        elif a1 == "BK":
            b2 = int(b2)
            key2 = int(key2)
            if (b1 == key0 and (b2 == key2+1 or b2 == key2-1)) or (b2 == key2 and (b3 == key6-1 or b3 == key6+1)) or (b3 == key6-1 and (b2 == key2+1 or b2 == key2-1)) or (b2 == key2+1 and (b2 == key2+1 or b2 == key2-1)):
                squares[b] = a
                squares[key1] = "   "
            else:
                continue  
        break
while True:
    if "WK " in squares.values() and "BK " in squares.values():
        a = input("pieces : ")
        b = input("square : ")
        user_turn(a,b,squares)
        print_squares(squares)
        bot_turn(squares)
        print_squares(squares)
    else:
        print("done!!!")
        break