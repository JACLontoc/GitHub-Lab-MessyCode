#Adds the two inputted numbers together as the sum function.
def sum(firstNumber,secondNumber):
  return firstNumber + secondNumber

#main function
def main( ):

  #Displays the program description.
  print("\nThis is a simple adder program.\n")

  #Only allows the input of integers
  try:
    firstNumber = int(input("Enter first number: "))
    secondNumber = int(input("Enter second number: "))

  #If the one of the inputs is not an integer it will consider it as an error and repeat the program
  except ValueError:
    print("Please input number!")
    main()

  #If the inputs are integers it will add the numbers and print
  else:
    print("The sum is:",sum(firstNumber,secondNumber))
    
#Calls the function at the end.
main( )