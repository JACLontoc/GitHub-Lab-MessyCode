# A simple program that adds two numbers and prints the result

def addNumbers(firstNumber, secondNumber):
  # Returns the sum of two numbers from user input
  return firstNumber + secondNumber

def main():
    # Display the description of the program
    print("\nThis is a simple adder program.\n")
    
    # Enter numbers by user to add using the program
    firstNumber = input("> Enter first number: ")
    secondNumber = input("> Enter second number: ")
    
    # Call the function to add the two numbers from user input
    addResult = addNumbers(int(firstNumber), int(secondNumber))
      
    # Print the result of the addition of two numbers from user input
    print(f"\nThe sum of {firstNumber} and {secondNumber} is:", addResult, "\n")

# Call the main function to start the program
main()

