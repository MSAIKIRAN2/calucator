def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def modulo(a,b):
    return a % b
def divide(a,b):
    return a / b
    
while True:
    num1 = float(input("enter the frist number: "))
    num2 = float(input("enter the second number: "))
    operator = input("enter an operator(+,-,*,/,%): ")
    if  operator == "+":
         result = add(num1,num2)
    elif  operator == "-":
          result = subtract(num1,num2)
    elif  operator == "*":
          result = multiply(num1,num2)
    elif  operator == "/":
          result = divide(num1,num2)
    elif  operator == "%":
          result = modulo(num1,num2)
    else:
        print("invalid operator")
        continue
    print(f"result: {num1} {operator} {num2} = {result}")
        


