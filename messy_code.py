def add_numbers(num1: float, num2: float) -> float:
    return num1 + num2

def get_number(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("=== Simple Adder Program ===")
    first_number = get_number("Enter first number: ")
    second_number = get_number("Enter second number: ")
    result = add_numbers(first_number, second_number)
    print(f"The sum is: {result}")

if __name__ == "__main__":
    main()