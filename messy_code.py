# Improved Adder Program

def add_numbers(num1, num2):
    return num1 + num2

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    print(" Welcome to the Simple Adder Program ")
    
    first_number = get_integer_input("Enter the first number: ")
    second_number = get_integer_input("Enter the second number: ")
    
    result = add_numbers(first_number, second_number)
    print(f"The sum is: {result}")

if __name__ == "__main__":
    main()