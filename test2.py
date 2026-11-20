def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("add")
print("subtract")
print("multiply")
print("divide")


try:
    choice = input("pick an operation (1-4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter first number: "))

    if choice == "1":
        print("result:", add(num1, num2))
    elif choice == "2":
        print("result:", subtract(num1, num2))
    elif choice == "3":
        print("result:", multiply(num1, num2))
    elif choice == "4":
        print("result:", divide(num1, num2))

except ValueError:
    print("Invalid input.")

except ZeroDivisionError:
    print("you cannot divide by zero")