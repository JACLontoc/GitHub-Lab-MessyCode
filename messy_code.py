def add_numbers(num1, num2):
    """Adds two numbers together."""
    return num1 + num2

def main():
    print("This is a simple adder program.")
    
    try:
        #first number
        a_input = input("Enter first number: ")
        num_a = int(a_input)
        
        #second number
        b_input = input("Enter second number: ")
        num_b = int(b_input)
        
        #calculate
        result = add_numbers(num_a, num_b)
        print(f"The sum is: {result}")

    except ValueError:
        #if letter enter
        print("Error: Please enter valid numbers only.")

# Only run main() if the script is executed directly
if __name__ == "__main__":
    main()