#Shan
def add_numbers(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2

#Jared
def get_valid_number(prompt):
    """Prompts the user until a valid integer is entered."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


#Dan Justine
def main():
    print("Welcome to the Simple Adder Program!")
    
    first_number = get_valid_number("Enter the first number: ")
    second_number = get_valid_number("Enter the second number: ")
  
   
    result = add_numbers(first_number, second_number)
    print(f"The sum is: {result}")

main()