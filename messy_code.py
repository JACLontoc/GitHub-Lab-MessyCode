"""
Simple Adder Program
--------------------
This program asks the user for two numbers,
adds them together, and displays the result.
"""

def add_numbers(num1, num2):
    """Return the sum of two numbers."""
    return num1 + num2


def main():
    print("=== Simple Adder Program ===")

    try:
        # Get user input and validate
        first_input = input("Enter the first number: ")
        second_input = input("Enter the second number: ")

        # Try converting inputs to integers
        num1 = int(first_input)
        num2 = int(second_input)

        # Compute sum
        result = add_numbers(num1, num2)

        # Display result
        print(f"The sum of {num1} and {num2} is: {result}")

    except ValueError:
        # Handle non-numeric input
        print("❌ Error: Please enter valid numbers only.")

    except Exception as e:
        # Handle any unexpected errors
        print(f"⚠️ An unexpected error occurred: {e}")


# Call the main function
if __name__ == "__main__":
    main()
