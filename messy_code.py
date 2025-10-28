# This program adds two numbers and prints the result

def add_numbers(a, b):
    return a + b

def main():
    print("Simple Adder Program")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = add_numbers(a, b)
    print("The sum is:", result)

main()
