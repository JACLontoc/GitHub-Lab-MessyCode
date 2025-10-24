def main():
  def addnumb(x, y):
    return x + y
  
  try:
    print("This is a simple adder program!")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
  except ValueError:
    print("Invalid input. Please enter numeric (0-9) values.")
    return

  sum = addnumb(a, b)
  print(f"The sum of {a} and {b} is: {sum}")

main()
