# After: clear names with validation
"""
Simple Number Adder Program
This program takes two numbers from the user and displays their sum.
"""

def add_numbers(first_number, second_number):
    """
    Add two numbers together and return the result.
    
    Args:
        first_number (int/float): The first number to add
        second_number (int/float): The second number to add
    
    Returns:
        int/float: The sum of the two numbers
    """
    return first_number + second_number


def main():
    """Main function to run the number adder program."""
    print("=" * 40)
    print("Simple Number Adder Program")
    print("=" * 40)
    
    try:
        # Get first number with input validation
        first_input = input("\nEnter the first number: ")
        first_number = float(first_input)
        
        # Get second number with input validation
        second_input = input("Enter the second number: ")
        second_number = float(second_input)
        
        # Calculate the sum
        result = add_numbers(first_number, second_number)
        
        # Display the result
        print("\n" + "-" * 40)
        print(f"The sum is: {result}")
        print("-" * 40)
        
    except ValueError:
        # Error handling for invalid input
        print("\nError: Please enter valid numbers only!")
        print("The program will now exit.")
    
    except Exception as error:
        # Catch any other unexpected errors
        print(f"\nAn unexpected error occurred: {error}")


# Call the main function to start the program
if __name__ == "__main__":
    main()
