number1 = float(input("enter the first number : "))
number2 = float(input("enter the second number : "))
sign = input("enter the operation : ")

if sign == "+" :
    result = number1 + number2
    print(result)
elif sign == "*" :
    result = number1 * number2
    print(result)
elif sign == "-" :
    result = number1 - number2
    print(result)
elif sign == "/" :
    result = number1 / number2
    print(result)
else :
    print("wrong operation")

