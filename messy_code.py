# This program adds two numbers and prints the result

def addNumbers(firstNumber, secondNumber):
    sum = firstNumber + secondNumber
    return sum

def main():
    while True:
        try:
            print("Simple Adder Program")
            firstNumber = int(input("Enter first number: "))
            secondNumber = int(input("Enter second number: "))
            result = addNumbers(firstNumber, secondNumber)
            print("The sum is:", result)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

main()
