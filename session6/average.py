a = int(input("how many number do you want to enter ? "))
sum = 0
print("enter the numbers")
for i in range(a) :
    number = float(input())
    sum = sum + number

avg = sum / a
print("average = " , avg)