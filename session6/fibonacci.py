
n = int(input("how many numbers of fibonacci do you want?"))
a = 0
b = 1
print(a)
print(b)
for i in range(n - 2) :
    c = a+b
    a = b
    b = c
    print(c)