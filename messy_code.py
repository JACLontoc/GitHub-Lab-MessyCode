# Trinidad added the function which will return the sum of 2 numbers

def add_numbers(num1, num2):
    """Return the sum of two numbers."""
    return num1 + num2

# Manilla added the function where prompt the user if s/he input an invalid number
def get_number(prompt):
    """Prompt the user for a number and validate the input."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Tagab added the main function which will collab the other two funtions, that will make the system whole
def main():
    """Main function to run the simple adder program."""
    print("=== Simple Adder Program ===")

    # Get validated input from user
    first_number = get_number("Enter the first number: ")
    second_number = get_number("Enter the second number: ")

    # Calculate and display the result
    result = add_numbers(first_number, second_number)
    print(f"The sum is: {result}")


# Call the main function directly
main()
