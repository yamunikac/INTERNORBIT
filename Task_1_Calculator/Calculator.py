# Task 1: Simple Calculator
# InternOrbit Python Programming Internship


print("====================================")
print("        SIMPLE CALCULATOR            ")
print("====================================")

while True:
    num1 = float(input("\nEnter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("\nChoose an operation:")
    print("Addition (+)")
    print("Subtraction (-)")
    print("Multiplication (*)")
    print("Division (/)")
    choice = input("Enter the operation symbol (+, -, *, /): ")
    if choice == "+":
        print("Result:", num1 + num2)
    elif choice == "-":
        print("Result:", num1 - num2)
    elif choice == "*":
        print("Result:", num1 * num2)
    elif choice == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed")
    else:
        print("Invalid operation! Please choose a valid symbol.")

    again = input("\nDo you want to perform another calculation? (yes/no): ")
    if again.lower() != "yes":
        print("\nThank you for using the Simple Calculator!")
        break
