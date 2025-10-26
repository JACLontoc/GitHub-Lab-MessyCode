
def addnumb(a, b):
    return a + b

def main():
    print("This is a simple adder program")
    a = input("Enter first number: ")
    b = input("Enter second number: ")

    try:
        res = addnumb(int(a), int(b))
        print("The sum is:", res)
    except ValueError:
        print("Please enter valid numbers only.")

if __name__ == "__main__":
    main()
