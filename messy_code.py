

def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

def main():
    print("This is a simple adder program.")
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        result = add_numbers(a, b)
        print("The sum is:", result)
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

if __name__ == "__main__":
    main()
