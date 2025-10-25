#this program add numbers and print the result but its not  messy anymore

def addnumb(a,b):return a+b

def main( ):
  print("------------------------------")
  print("This is a simple adder program")
  print("------------------------------")
  while True:
    try:
        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))
        
        break  
    except ValueError:
      
        print("Invalid input! Please enter a valid number.")

        
        
  res=(int(a)+ int(b))
      
  print("the sum is: ", res)

  
main( )
