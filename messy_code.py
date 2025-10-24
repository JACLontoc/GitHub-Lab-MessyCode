# messy_code.py
# This program adds two numbers entered by the user.

def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


def main():
    print("=== Simple Adder Program ===")

    try:
        # Get user inputs with validation
        a = input("Enter first number: ")
        b = input("Enter second number: ")

        # Convert to integers
        num1 = int(a)
        num2 = int(b)

        # Calculate and display result
        result = add_numbers(num1, num2)
        print(f"The sum of {num1} and {num2} is: {result}")

    except ValueError:
        print("Error: Please enter valid numbers only.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the program
if __name__ == "__main__":
    main()
