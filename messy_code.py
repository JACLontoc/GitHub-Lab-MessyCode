#This program adds numbers and prints the sum

def addNumbers(a,b):return a+b
def main( ):
    print("This is a simple adder program")
    firstNum=input("enter first number: ")
    secondNum=input("enter second number: ")
    sum=addNumbers(int(firstNum),int(secondNum))
    print("the sum is :",sum)
main( )#calls the function
