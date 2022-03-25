def calc(num1,num2,op):
    if op == "+":
        return num1+num2
    elif op == "-":
        return num1-num2
    elif op == "*":
        return num1*num2
    elif op == "/":
        return num1/num2

number1 = ''
while number1 is not float:
    try:
        number1 = float(input('Enter a number: '))
        break
    except ValueError:
        print('Please enter a valid number: ')
        
operator = input("Masukan operasi :")
while operator != "+" and operator != "-" and operator != "*" and operator != "/":
        operator = input("Masukan bukan simbol operasi :")

number2 = ''
while number2 is not float:
    try:
        number2 = float(input('Enter a number: '))
        break
    except ValueError:
        print('Please enter a valid number: ')
print (number1, operator, number2, "=", calc(number1, number2, operator))