def add(x, y):
    """Add two numbers and return the result."""
    return x + y

def subtract(x, y):
    """Subtract second number from first and return the result."""
    return x - y

def multiply(x, y):
    """Multiply two numbers and return the result."""
    return x * y

def divide(x, y):
    """Divide first number by second and return the result.
    Returns None if division by zero is attempted."""
    if y == 0:
        return None
    return x / y

def main():
    """Main calculator program."""
    print("*** Welcome to Basic Calculator ***")
    print("Choose a mathematical operation:")
    userChoice = input("(1) Add two numbers\n(2) Subtract two numbers\n(3) Multiply two numbers\n(4) Divide two numbers\n")

    try:
        firstNumber = float(input("Type the first number: "))
        secondNumber = float(input("Type the second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    match userChoice:
        case "1":
            result = add(firstNumber, secondNumber)
            print(f"The addition of {firstNumber} and {secondNumber} is {result}")
        case "2":
            result = subtract(firstNumber, secondNumber)
            print(f"The subtraction of {firstNumber} and {secondNumber} is {result}")
        case "3":
            result = multiply(firstNumber, secondNumber)
            print(f"The multiplication of {firstNumber} and {secondNumber} is {result}")
        case "4":
            result = divide(firstNumber, secondNumber)
            if result is None:
                print("Error: Division by zero is not allowed!")
            else:
                print(f"The division of {firstNumber} and {secondNumber} is {result}")
        case "5":
            result = power(firstNumber, secondNumber)
            print(f"{firstNumber} to the power of {secondNumber} is {result}")
        case _:
            print("Invalid menu choice.")

# Run the calculator if this file is executed directly
if __name__ == "__main__":
    main()