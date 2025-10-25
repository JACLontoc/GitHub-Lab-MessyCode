# Summation of two numbers.
def calculateSum(firstNumber, secondNumber):
  return firstNumber + secondNumber


# Main Program
def main( ):
  print("This is a simple adder program. \n")

  try:
    firstNumber = float(input("Enter first number: "))
    secondNumber = float(input("Enter second number: "))

    sum = calculateSum(firstNumber, secondNumber)

    print("\n The sum is :", sum)

  except ValueError:
    print("Value Error: Please input a valid number.")


# Call the function at end.
main() 
