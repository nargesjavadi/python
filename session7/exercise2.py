def avg(a):
    sum = 0
    for i in a :
        sum = i + sum
    average = sum / len(a)
    return average

def min(a):
    min = a[0]
    for i in a :
        if i < min:
            min = i
    return min

def max(a):
    max = a[0]
    for i in a :
        if i > max:
            max = i
    return max

def var(a):
    sum = 0
    for i in a :
        variance = (i - avg(a)) ** 2
        sum = variance + sum
    vari = sum / len(a)
    return vari

number = [3,2,1]
output = avg(number)
print("average: ",output)

number = [3,2,1]
output = min(number)
print("min: ",output)

number = [3,2,1]
output = max(number)
print("max: ",output)

number = [5,7,3,7,8]
output = var(number)
print("variance: ",output)