# Simple Addition Program
# Author: Sai

def add_numbers(firstNum, secNum):
    # Return the sum of two numbers.
    return firstNum + secNum

def main():
    print("=== Simple Addition Program ===")
    
    # Get user input
    firstNum = int(input("Enter first number: "))
    secNum = int(input("Enter second number: "))
    
    # Compute and display result
    result = add_numbers(firstNum, secNum)
    print(f"The sum is: {result}")
    
main()