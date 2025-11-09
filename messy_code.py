# This program adds two user-provided numbers and prints the result.

def add_numbers(num1, num2):
    return num1 + num2

def main():
    """main function to handle input, validation, and output."""

    print("\n--- This is a simple adder program ---")

    # use a loop for continuous input until valid numbers are entered
    while True:
        try:
            first_num = float(input("Enter the first number: "))
            second_num = float(input("Enter the second number: "))
            break  #exit the loop only if both inputs are successfully converted to float

        except ValueError:
            #error handling
            print("Invalid input! Please enter a valid number.")

    #perform the calculation after successful input and inside main()
    sum_result = add_numbers(first_num, second_num)

    #show the result
    print(f"The sum is: {sum_result}")

main()