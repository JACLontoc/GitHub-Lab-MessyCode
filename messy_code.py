#This program adds numbers and prints the sum
def addNumbers(a,b):
    return a+b

def main( ):
    print("This is a simple addition program.")
    try:
        firstNum=int(input("Enter first number: "))
        secondNum=int(input("Enter second number: "))
        totalAdd=addNumbers((firstNum),(secondNum))
        print("The sum is :",totalAdd)
    except ValueError:
      print("Value Error. Please try again")
       
main( )#Calls the function 