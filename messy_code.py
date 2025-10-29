def add_numbers(num1, num2):
    #Return the sum of two numbers 
    return num1 + num2


def get_number(prompt):
    # Prompt the user for a number and validate input.
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def main():
    # Main function to run the adder program.
    print("Simple Addition Calculator")

    number1 = get_number("Enter the first number: ")
    number2 = get_number("Enter the second number: ")

    total = add_numbers(number1, number2)
    print(f"The sum is: {total}")


# Call the main function directly
main()

