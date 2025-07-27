x1 = float(input("origin x : "))
y1 = float(input("origin y : "))
x2 = float(input("destination x : "))
y2 = float(input("destination y : "))
v = float(input("velocitas : "))
a = ((x2-x1)**2)+((y2-y1)**2)
import math
d = math.sqrt(a)
t = d/v
print("distance = " , d)
print("time = " , t)