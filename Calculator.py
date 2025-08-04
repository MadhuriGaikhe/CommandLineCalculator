
def Calculator(n1,n2,op):
    if op == '+':
        result = n1 + n2
        return result
    elif op == '-':
        result = n1 - n2
        return result
    elif op == '/':
        result = n1 / n2
        return result
    elif op == '*':
        result = n1 * n2
        return result
    else:
        result = print("Invalid Operator Please use +, -, *, or /.")
        return result

try:
    num1 = float(input("Enter First Number: "))
    op = input("Enter a Operator (+,-,/,*): ")
    num2 = float(input("Enter Second Number: "))

    print(num1,op,num2)
    result = Calculator(num1,num2,op)
    print("Calculation is: ",result)

except ValueError:
     print("Invalid input. Please enter valid numbers.")