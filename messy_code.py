#this program add numbers and print the result but its really messy

def Addition(num1,num2):
	return num1 + num2

def EnterNumber():
	try:
		num1 = int(input("Enter First Number: "))
		num2 = int(input("Enter Second Number: "))
	except:
		print("Please input numbers")
	return num1,num2


def main( ):
  print("This is a simple adder program")
  a=input("enter first number")
  b=input("enter second number")
  res=addnumb(int(a),int(b))
  print("the sum is :",res)

main( )#call the function at end
# KELVIN CODE