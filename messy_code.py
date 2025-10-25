def add_numbers(a, b):
    return a + b

def main():
    print("This is a simple adder program")
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = add_numbers(a, b)
        print("The sum is:", result)
    except ValueError:
        print("Please enter valid numbers only.")

if __name__ == "__main__":
    main()
