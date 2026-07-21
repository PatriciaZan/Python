

operator = input("Enter an operator (+ - * / )")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print("The sum is", result)
elif operator == "-":
    result = num1 - num2
    print("The difference is", result)
elif operator == "*":
    result = num1 * num2
    print("The multiplication is", result)
elif operator == "/":
    result = num1 / num2
    print("The division is", result)
else:
    print(f"Invalid operator -> {operator}")

