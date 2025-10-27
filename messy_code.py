# This program adds two numbers and prints the result
def add_numbers(a, b):
    return a + b

def main():
    print("This is a simple adder program")

    while True:
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            break  # exit the loop only if both inputs are valid
        except ValueError:
            print("Invalid input! Please enter numeric values only.\n")

    result = add_numbers(a, b)
    print("The sum is:", result)


if __name__ == "__main__":
    main()
