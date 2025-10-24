#This program simply adds two positive numbers provided by the user and displays the result.

def main( ):
  def addNum(a, b): #function to add two numbers
    sum = a + b
    return sum
  
  try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if a < 0 or b < 0:
      raise ValueError
    
  except ValueError:
    print("Invalid input. Please enter positive integers only.")
    return

  print("\nThis is a simple program that adds two positive numbers.")
  print(f"The sum of {a} and {b} is {addNum(a, b)}")
  
main()