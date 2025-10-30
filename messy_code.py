def add_numbers(a, b):
    return a + b

def main():
    print("\nThis is my simple adder program!\n")
    
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = add_numbers(a, b)

    print(rf"""
  _____________________
 |  _________________  |
 | | {a} + {b} = {result:<8}| |   
 | |_________________| |
 |  ___ ___ ___        |
 | | 7 | 8 | 9 |       |
 | |___|___|___|       |
 | | 4 | 5 | 6 |       |
 | |___|___|___|       |
 | | 1 | 2 | 3 |       |
 | |___|___|___|  ___  |
 | | . | 0 | = | | + | |
 | |___|___|___| |___| |
 |_____________________|
        
""")

main()