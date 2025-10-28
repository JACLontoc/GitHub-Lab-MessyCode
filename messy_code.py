# Simple program to add two numbers and display the result

def add_numbers(first_number, second_number):
    """Add two numbers and return the result."""
    return first_number + second_number


def main():
    """Main function to run the addition program."""
    print("This is a simple adder program")
    
    try:
        # Get user input
        first_input = input("Enter first number: ")
        second_input = input("Enter second number: ")
        
        # Validate and convert inputs to integers
        first_number = int(first_input)
        second_number = int(second_input)
        
        # Calculate and display result
        result = add_numbers(first_number, second_number)
        print(f"The sum is: {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers only.")


# Run the program
main()