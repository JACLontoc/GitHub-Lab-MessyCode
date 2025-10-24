#this program add numbers and print the result but its really messy

def addnumb(a,b):return a + b
    
def main( ):
  print("This is a simple adder program")

  while True:
    a = input("[Input first number]: ")
    if a.isdigit():
      break
    print("[Must be an integer.]")


  while True:
    b = input("[Input second number]:" )
    if b.isdigit():
      break
    print("[Must be an integer.]")


  res=addnumb(int(a), int(b))
  print("[The sum is]: ",res)

main( )#call the function at end
# KELVIN CODE