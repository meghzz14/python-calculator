print("Welcome to the Python Calculator!")

while True:
    # Step 1: Get two numbers from the user
    try:
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue  # Ask again

    # Step 2: Show operations
    print("\nChoose an operation:")
    print("+ : Addition")
    print("- : Subtraction")
    print("* : Multiplication")
    print("/ : Division")
    print("% : Modulus")
    print("** : Exponentiation")
    print("q : Quit")  # option to exit

    operation = input("Enter operation symbol: ")

    # Step 3: Check for quit option
    if operation.lower() == "q":
        print("Thank you for using the calculator. Goodbye!")
        break

    # Step 4: Perform calculation with error handling
    try:
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        elif operation == "%":
            result = num1 % num2
        elif operation == "**":
            result = num1 ** num2
        else:
            print("Invalid operation! Please choose a valid symbol.")
            continue  # Restart loop if invalid
    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")
        continue  # Restart loop

    # Step 5: Show result
    print(f"The result of {num1} {operation} {num2} is: {result} Thank you for using the calculator. Goodbye!")

