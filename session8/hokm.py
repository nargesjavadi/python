import random
import numpy

def dealing() :
    a = []
    for i in range(5):
        x = random.choice(cards)
        a.append(x)
        n = cards.index(x)
        cards.pop(n)
    return a
def dealing2(a) :
    for i in range(4):
        x = random.choice(cards)
        a.append(x)
        n = cards.index(x)
        cards.pop(n)
    return a

def ChooseTrump(a):
    sdel = 0
    spic = 0
    sgish = 0
    skhesht = 0
    for i in a:
        rank,suit = i.split()
        rank = int(rank)
        if suit == "del":
            sdel = sdel + rank
        elif suit == "pic":
            spic = spic + rank
        elif suit == "gish":
            sgish = sgish + rank
        elif suit == "khesht":
            skhesht = skhesht + rank
    sum = [sdel , spic , sgish , skhesht]
    max = sum[0]
    for i in sum :
        if i > max :
            max = i
    l = sum.index(max)
    if l == 0 :
        final = "del"
    elif l == 1 :
        final = "pic"
    elif l == 2 :
        final = "gish"
    elif l == 3 :
        final = "khesht"

    return final

def FirstChoice(a,b,c,d,e,trump):
    sdel = 0
    spic = 0
    sgish = 0
    skhesht = 0
    for i in a:
        rank,suit = i.split()
        rank = int(rank)
        if suit == "del":
            sdel = sdel + rank
        elif suit == "pic":
            spic = spic + rank
        elif suit == "gish":
            sgish = sgish + rank
        elif suit == "khesht":
            skhesht = skhesht + rank
    if trump == "del":
        if sdel >= 50:
            return b[0]
    if trump == "pic":
        if spic >= 50:
            return c[0]
    if trump == "gish":
        if sgish >= 50:
            return d[0]
    if trump == "khesht":
        if skhesht >= 50:
            return e[0]
    if "14 del" in b:
            return b[-1] 
    if "14 pic" in c:
            return c[-1]
    if "14 gish" in d:
            return d[-1]
    if "14 khesht" in e:
            return e[-1]
    if len(b) == 1 and trump != "del":
        return b[0]
    if len(c) == 1 and trump != "pic":
        return c[0]
    if len(d) == 1 and trump != "gish":
        return d[0]
    if len(e) == 1 and trump != "khesht":
        return e[0]
    if len(b) == 2 and trump != "del":
        return b[0]
    if len(c) == 2 and trump != "pic":
        return c[0]
    if len(d) == 2 and trump != "gish":
        return d[0]
    if len(e) == 2 and trump != "khesht":
        return e[0]
    if len(b) == 3 and trump != "del":
        return b[0]
    if len(c) == 3 and trump != "pic":
        return c[0]
    if len(d) == 3 and trump != "gish":
        return d[0]
    if len(e) == 3 and trump != "khesht":
        return e[0]
    if a:
        while True:
            choice = random.choice(a)
            rank,suit = choice.split()
            if suit != trump:
                return choice

def SecondChoice(FirstTurn ,trump,a,b,c,d,e , m):  
    rank,suit = FirstTurn.split()
    if suit == "del":
        if "14 del" in b:
            return b[-1]
        elif (rank == "14" or rank == "13") and len(b) > 0:
            return b[0]
        elif len(b) > 0:
            return b[0]
        else :
            if len(m+trump+"Cards") > 0:
                return m+trump+"Cards"[0]
            else:
                return random.choice(a)
    if suit == "pic":
        if "14 pic" in c:
            return c[-1]
        if (rank == "14" or rank == "13") and len(c) > 0:
            return c[0]
        if len(c) > 0:
            return c[0]
        else:
            if len(m+trump+"Cards") > 0:
                return m+trump+"Cards"[0]
            else:
                return random.choice(a)
    if suit == "gish":
        if "14 gish" in d:
            return d[-1]
        if (rank == "14" or rank == "13") and len(d) > 0:
            return d[0]
        if len(d) > 0:
            return d[0]
        else:
            if len(m+trump+"Cards") > 0:
                return m+trump+"Cards"[0]
            else:
                return random.choice(a)
    if suit == "khesht":
        if "14 khesht" in e:
            return e[-1]
        if (rank == "14" or rank == "13") and len(e) > 0:
            return e[0]
        if len(e) > 0:
            return e[0]
        else:
            if len(m+trump+"Cards") > 0:
                return m+trump+"Cards"[0]
            else:
                return random.choice(a)

def ThirdChoice(FirstTurn , SecondTurn ,trump,a,b,c,d,e ,m):
    rank,suit = FirstTurn.split()
    rank = int(rank)
    rank2,suit2 = SecondTurn.split()
    rank2 = int(rank2)
    if suit == "del":
        if len(b) > 0:
            rankb,suitb = b[-1].split()
            rankb = int(rankb)
            if rank > rankb:
                return b[0]
            else:
                if rank2 > rankb:
                    return b[0]
                else:
                    if "14 del" in b:
                        return b[-1]
                    if "13 del" in b:
                        return b[-1]
                    if "12 del" in b:
                        return b[-1]
                    if b:
                        return b[0]
        else:
            if len(m+trump+"Cards") > 0:
                return m+trump+"Cards"[0]
            else:
               return random.choice(a)
    if suit == "pic":
        if len(c) > 0:
            rankc,suitc = c[-1].split()
            rankc = int(rankc)
            if rank > rankc:
                return c[0]
            else:
                if rank2 > rankc:
                    return c[0]
                else:
                    if "14 pic" in c:
                        return c[-1]
                    if "13 pic" in c:
                        return c[-1]
                    if "12 pic" in c:
                        return c[-1]
                    if c:
                        return c[0]
        else:
            if len(m+trump+"Cards") > 0:
                return m+trump+"Cards"[0]
            else:
               return random.choice(a)
    if suit == "gish":
        if len(d) > 0:
            rankd,suitd = d[-1].split()
            rankd = int(rankd)
            if rank > rankd:
                return d[0]
            else:
                if rank2 > rankd:
                    return d[0]
                else:
                    if "14 gish" in d:
                        return d[-1]
                    if "13 gish" in d:
                        return d[-1]
                    if "12 gish" in d:
                        return d[-1]
                    if d:
                        return d[0]
        else:
            if len(m+trump+"Cards") > 0:
                return m+trump+"Cards"[0]
            else:
               return random.choice(a)
    if suit == "khesht":
        if len(e) > 0:
            ranke,suite = e[-1].split()
            ranke = int(ranke)
            if rank > ranke:
                return e[0]
            else:
                if rank2 > ranke:
                    return e[0]
                else:
                    if "14 khesht" in e:
                        return e[-1]
                    if "13 khesht" in e:
                        return e[-1]
                    if "12 khesht" in e:
                        return e[-1]
                    if e:
                        return e[0]
        else:
            if len(m+trump+"Cards") > 0:
                return m+trump+"Cards"[0]
            else:
               return random.choice(a)   

def ForthCoice(FirstTurn , SecondTurn, ThirdTurn ,trump,a,b,c,d,e ,m):
    rank,suit = FirstTurn.split()
    rank = int(rank)
    rank2,suit2 = SecondTurn.split()
    rank2 = int(rank2)
    rank3,suit3 = ThirdTurn.split()
    rank3 = int(rank3)   
    if suit == "del":
        if len(b) > 0:
            if rank2 > rank and rank2 > rank3:  
                return b[0]
            else:
                rankb,suitb = b[-1].split()
                rankb = int(rankb)
                if rankb >rank and rankb>rank3:
                    return b[-1]
                else:
                    return random.choice(b)   
        else:
            if len(m+trump+"Cards") > 0:
                return m+trump+"Cards"[0]
            else:
               return random.choice(a)
    if suit == "pic":
        if len(c) > 0:
            if rank2 > rank and rank2 > rank3:  
                return c[0]
            else:
                rankc,suitc = c[-1].split()
                rankc = int(rankc)
                if rankc >rank and rankc>rank3:
                    return c[-1]
                else:
                    return random.choice(c)   
        else:
            if len(m+trump+"Cards") > 0:
                return m+trump+"Cards"[0]
            else:
               return random.choice(a)
    if suit == "gish":
        if len(d) > 0:
            if rank2 > rank and rank2 > rank3:  
                return d[0]
            else:
                rankd,suitd = d[-1].split()
                rankd = int(rankd)
                if rankd >rank and rankd>rank3:
                    return d[-1]
                else:
                    return random.choice(d)   
        else:
            if len(m+trump+"Cards") > 0:
                return m+trump+"Cards"[0]
            else:
               return random.choice(a)
    if suit == "khesht":
        if len(e) > 0:
            if rank2 > rank and rank2 > rank3:  
                return e[0]
            else:
                ranke,suite = e[-1].split()
                ranke = int(ranke)
                if ranke >rank and ranke>rank3:
                    return e[-1]
                else:
                    return random.choice(e)   
        else:
            if len(m+trump+"Cards") > 0:
                return m+trump+"Cards"[0]
            else:
               return random.choice(a)  

def getnumber(a):
    return int(a.split()[0])
def sortcards(a):
    sorteddel = []
    sortedkhesht = []
    sortedgish = []
    sortedpic = []
    for i in a:
        rank,suit = i.split()
        if suit == "del":
            sorteddel.append(i)
            sorteddel.sort(key=getnumber)
        elif suit == "khesht":
            sortedkhesht.append(i)
            sortedkhesht.sort(key=getnumber)
        elif suit == "gish":
            sortedgish.append(i)
            sortedgish.sort(key=getnumber)
        elif suit == "pic":
            sortedpic.append(i)
            sortedpic.sort(key=getnumber)
    return sorteddel , sortedkhesht , sortedgish , sortedpic
    
def choosePlayer():
    global Firstplayer , SecondPlayer , ThirdPlayer , FourthPlayer
    if dealer == "user":
        Firstplayer = "user"
        SecondPlayer = "bot1"
        ThirdPlayer = "bot2"
        FourthPlayer = "bot3"
    elif dealer == "bot1":
        Firstplayer = "bot1"
        SecondPlayer = "bot2"
        ThirdPlayer = "bot3"
        FourthPlayer = "user"
    elif dealer == "bot2":
        Firstplayer = "bot2"
        SecondPlayer = "bot3"
        ThirdPlayer = "user"
        FourthPlayer = "bot1"
    elif dealer == "bot3":
        Firstplayer = "bot3"
        SecondPlayer = "user"
        ThirdPlayer = "bot1"
        FourthPlayer = "bot2"

def winer(FirstTurn , SecondTurn, ThirdTurn , ForthTurn,trump):
    rank,suit = FirstTurn.split()
    rank = int(rank)
    rank2,suit2 = SecondTurn.split()
    rank2 = int(rank2)
    rank3,suit3 = ThirdTurn.split()
    rank3 = int(rank3)
    rank4,suit4 = ForthTurn.split()
    rank4 = int(rank4)
    a = [rank,rank2,rank3,rank4]
    w = numpy.amax(a)
    if suit == suit2 and suit2 == suit3 and suit3 == suit4:
        if w == rank:
            return "FirstPlayer"
        if w == rank2:
            return "SecondPlayer"
        if w == rank3:
            return "ThirdPlayer"
        if w == rank4:
            return "ForthPlayer"
    if suit == trump:
        return "FirstPlayer"
    if suit2 == trump:
           return "SecondPlayer"
    if suit3 == trump:
        return "ThirdPlayer"
    if suit4 == trump:
        return "ForthPlayer"
        
cards = ["2 del","3 del","4 del","5 del","6 del","7 del","8 del","9 del","10 del","11 del","12 del","13 del","14 del",
         "2 pic","3 pic","4 pic","5 pic","6 pic","7 pic","8 pic","9 pic","10 pic","11 pic","12 pic","13 pic","14 pic",
         "2 khesht","3 khesht","4 khesht","5 khesht","6 khesht","7 khesht","8 khesht","9 khesht","10 khesht","11 khesht","12 khesht","13 khesht","14 khesht",
         "2 gish","3 gish","4 gish","5 gish","6 gish","7 gish","8 gish","9 gish","10 gish","11 gish","12 gish","13 gish","14 gish"]
player = ["bot1","bot2","bot3","user"]

dealer = random.choice(player)
print("dealer : ", dealer)

# choose trump

UserCards = dealing()
if dealer == "user":
    print("your cards : ",UserCards)
Bot1Cards = dealing()
Bot2Cards = dealing()
Bot3Cards = dealing()

if dealer =="user":
    trump = input("choose the trump : ")
elif dealer == "bot1":
    trump = ChooseTrump(Bot1Cards)
    print("trump : " , trump)
elif dealer == "bot2":
    trump = ChooseTrump(Bot2Cards)
    print("trump : " , trump)
elif dealer == "bot3":
    trump = ChooseTrump(Bot3Cards)
    print("trump : " , trump)

for i in range(2):
    UserCards = dealing2(UserCards)
    Bot1Cards = dealing2(Bot1Cards)
    Bot2Cards = dealing2(Bot2Cards)
    Bot3Cards = dealing2(Bot3Cards)

# start the game
i = 0
while i <= 13:
    UserdelCards ,UserkheshtCards ,UsergishCards ,UserpicCards = sortcards(UserCards)
    print("your cards : ",UserdelCards ,UserkheshtCards ,UsergishCards ,UserpicCards)
    Bot1delCards ,Bot1kheshtCards ,Bot1gishCards ,Bot1picCards = sortcards(Bot1Cards)
    # print("bot 1 cards : " , Bot1delCards ,Bot1kheshtCards ,Bot1gishCards ,Bot1picCards)
    Bot2delCards ,Bot2kheshtCards ,Bot2gishCards ,Bot2picCards = sortcards(Bot2Cards)
    # print("bot 2 cards : " , Bot2delCards ,Bot2kheshtCards ,Bot2gishCards ,Bot2picCards)
    Bot3delCards ,Bot3kheshtCards ,Bot3gishCards ,Bot3picCards = sortcards(Bot3Cards)
    # print("bot 3 cards : " , Bot3delCards ,Bot3kheshtCards ,Bot3gishCards ,Bot3picCards)
    choosePlayer()
    if Firstplayer == "user":
        Firstplayer = "user"
        FirstTurn = input("User : ")
        UserCards.pop(UserCards.index(FirstTurn))
    elif Firstplayer == "bot1":
        Firstplayer = "bot1"
        FirstTurn = FirstChoice(Bot1Cards,Bot1delCards,Bot1picCards,Bot1gishCards,Bot1kheshtCards,trump)
        print("bot1 : " ,FirstTurn)
        Bot1Cards.pop(Bot1Cards.index(FirstTurn))
    elif Firstplayer == "bot2":
        Firstplayer = "bot2"
        FirstTurn = FirstChoice(Bot2Cards,Bot2delCards,Bot2picCards,Bot2gishCards,Bot2kheshtCards,trump)
        print("bot2 : " ,FirstTurn)
        Bot2Cards.pop(Bot2Cards.index(FirstTurn))
    elif Firstplayer == "bot3":
        Firstplayer = "bot3"
        FirstTurn = FirstChoice(Bot3Cards,Bot3delCards,Bot3picCards,Bot3gishCards,Bot3kheshtCards,trump)
        print("bot3 : " ,FirstTurn)
        Bot3Cards.pop(Bot3Cards.index(FirstTurn))
    
    if SecondPlayer == "user":
        SecondPlayer = "user"
        SecondTurn = input("User : ")
        UserCards.pop(UserCards.index(SecondTurn))
    elif SecondPlayer == "bot1":
        SecondPlayer = "bot1"
        SecondTurn = SecondChoice(FirstTurn,trump,Bot1Cards,Bot1delCards,Bot1picCards,Bot1gishCards,Bot1kheshtCards,"Bot1")
        print("bot1 : " ,SecondTurn)
        Bot1Cards.pop(Bot1Cards.index(SecondTurn))
    elif SecondPlayer == "bot2":
        SecondPlayer = "bot2"
        SecondTurn = SecondChoice(FirstTurn,trump,Bot2Cards,Bot2delCards,Bot2picCards,Bot2gishCards,Bot2kheshtCards,"Bot2")
        print("bot2 : " ,SecondTurn)
        Bot2Cards.pop(Bot2Cards.index(SecondTurn))
    elif SecondPlayer == "bot3":
        SecondPlayer = "bot3"
        SecondTurn = SecondChoice(FirstTurn,trump,Bot3Cards,Bot3delCards,Bot3picCards,Bot3gishCards,Bot3kheshtCards,"Bot3")
        print("bot3 : " ,SecondTurn)
        Bot3Cards.pop(Bot3Cards.index(SecondTurn))

    if ThirdPlayer == "user":
        ThirdPlayer = "user"
        ThirdTurn = input("User : ")
        UserCards.pop(UserCards.index(ThirdTurn))
    elif ThirdPlayer == "bot1":
        ThirdPlayer = "bot1"
        ThirdTurn = ThirdChoice(FirstTurn,SecondTurn,trump,Bot1Cards,Bot1delCards,Bot1picCards,Bot1gishCards,Bot1kheshtCards,"Bot1")
        print("bot1 : " ,ThirdTurn)
        Bot1Cards.pop(Bot1Cards.index(ThirdTurn))
    elif ThirdPlayer == "bot2":
        ThirdPlayer = "bot2"
        ThirdTurn = ThirdChoice(FirstTurn,SecondTurn,trump,Bot2Cards,Bot2delCards,Bot2picCards,Bot2gishCards,Bot2kheshtCards,"Bot2")
        print("bot2 : " ,ThirdTurn)
        Bot2Cards.pop(Bot2Cards.index(ThirdTurn))
    elif ThirdPlayer == "bot3":
        ThirdPlayer = "bot3"
        ThirdTurn = ThirdChoice(FirstTurn,SecondTurn,trump,Bot3Cards,Bot3delCards,Bot3picCards,Bot3gishCards,Bot3kheshtCards,"Bot3")
        print("bot3 : " ,ThirdTurn)
        Bot3Cards.pop(Bot3Cards.index(ThirdTurn))

    if FourthPlayer == "user":
        FourthPlayer = "user"
        ForthTurn = input("User : ")
        UserCards.pop(UserCards.index(ForthTurn))
    elif FourthPlayer == "bot1":
        FourthPlayer = "bot1"
        ForthTurn = ForthCoice(FirstTurn,SecondTurn,ThirdTurn,trump,Bot1Cards,Bot1delCards,Bot1picCards,Bot1gishCards,Bot1kheshtCards,"Bot1")
        print("bot1 : " ,ForthTurn)
        Bot1Cards.pop(Bot1Cards.index(ForthTurn))
    elif FourthPlayer == "bot2":
        FourthPlayer = "bot2"
        ForthTurn = ForthCoice(FirstTurn,SecondTurn,ThirdTurn,trump,Bot2Cards,Bot2delCards,Bot2picCards,Bot2gishCards,Bot2kheshtCards,"Bot2")
        print("bot2 : " ,ForthTurn)
        Bot2Cards.pop(Bot2Cards.index(ForthTurn))
    elif FourthPlayer == "bot3":
        FourthPlayer = "bot3"
        ForthTurn = ForthCoice(FirstTurn,SecondTurn,ThirdTurn,trump,Bot3Cards,Bot3delCards,Bot3picCards,Bot3gishCards,Bot3kheshtCards,"Bot3")
        print("bot3 : " ,ForthTurn)
        Bot3Cards.pop(Bot3Cards.index(ForthTurn))
    
    winer = winer(FirstTurn,SecondTurn,ThirdTurn,ForthTurn,trump)
    if winer == "FirstPlayer":
        dealer = Firstplayer
    elif winer == "SecondPlayer":
        dealer = SecondPlayer
    elif winer == "ThirdPlayer":
        dealer = ThirdPlayer
    elif winer == "ForthPlayer":
        dealer = FourthPlayer
    i = i+1