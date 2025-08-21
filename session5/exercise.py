a = int(input("enter the first number"))
b = int(input("enter the second number"))
c = int(input("enter the third number"))
d = int(input("enter the fourth number"))

# max

if a > b :
    if a > c :
        if a > d :
            max = a
        else :
            max = d
    elif c > d :
        max = c
    else :
        max = d
elif b > c :
    if b > d :
        max = b
    else :
        max = d
elif c > d :
    max = c
else :
    max = d

print(max , "is the max")

# min

if a < b :
    if a < c :
        if a < d :
            min = a
        else :
            min = d
    elif c < d :
        min = c
    else :
        min = d
elif b < c :
    if b < d :
        min = b
    else :
        min = d
elif c < d :
    min = c
else :
    min = d

print(min , "is the min")    

# average

avg = (a+b+c+d)/ 4
print("average = " , avg)

#  variance

a = (a - avg) ** 2
b = (b - avg) ** 2
c = (c - avg) ** 2
d = (d - avg) ** 2

variance = (a+b+c+d) / 4
 
print("variance is ",variance)

#  standard deviation

import math
s = math.sqrt(variance)
print("standard deviation ", s )
