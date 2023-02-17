#calculator
number1 = eval(input("Enter first number:"))
number2 = eval(input("Enter second number:"))
               
operator = input("Enter operator: ") 
def add(num1, num2):
    result = num1 + num2
    print(result)

def subtract(num1, num2):
    result = num1 - num2
    print(result)


def divide(num1, num2):
    result = num1 / num2
    print(result)

def multiply(num1, num2):
    result =num1 * num2 
    print(result)

if operator == "+":
    add(number1, number2)
elif operator =="-":
    subtract(number1, number2)
elif operator =="/":
    divide(number1,number2)
elif operator == "X":
     multiply(number1, number2)
else:
    print("Invalid operator")