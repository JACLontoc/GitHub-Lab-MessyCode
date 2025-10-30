def add(numOne, numTwo):
    return numOne + numTwo

def main():
    print("Welcome! This is a simple addition program")
    firstNum = input("Please enter the first number: ")
    secondNum = input("Please enter the second number: ")
    if not firstNum.isdigit() or not secondNum.isdigit():
        print("Invalid input. Please enter numeric values only.")
        return main()
    else:
        print(f"The Sum is : {add(int(firstNum), int(secondNum))}")

main()
