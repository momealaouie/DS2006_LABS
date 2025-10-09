print("*** Welcome to Basic Calculator *** ")
print("Choose a mathematical operation: ")
userChoice = input("(1) Add two numbers\n (2) Subtract two numbers\n (3) Multiply two numbers\n (4) Divide two numbers\n")

firstNumber = input("Type the first number: ")
secondNumber = input("Type the second number: ")

match str(userChoice):
    case "1":
        total = firstNumber + secondNumber
        print(f"The addition of {firstNumber} and {secondNumber} is {total}")
    case "2":
        total = firstNumber - secondNumber
        print(f"The subtraction of {firstNumber} and {secondNumber} is {total}")
    case "3":
        total = firstNumber * secondNumber
        print(f"The multiplication of {firstNumber} and {secondNumber} is {total}")
    case "4":
        total = firstNumber / secondNumber
        print(f"The division of {firstNumber} and {secondNumber} is {total}")
    case _:
        print("Invalid menu choice. ")