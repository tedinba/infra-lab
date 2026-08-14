from calculator.operations import add, subtract, multiply, divide

def get_numbers():
    first = float(input("First number: "))
    second = float(input("Second number: "))
    return first, second 

def main():
   while True:
        print("Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an operation: ")

        if choice == "1":
            try:
                first, second = get_numbers()
                result = add(first, second)
                print(f"Result: {result}")
            except ValueError:
                print("Error: Please enter valid numbers.")
        elif choice == "2":
            try:
                first, second = get_numbers()
                result = subtract(first, second)
                print(f"Result: {result}")
            except ValueError:
                print("Error: Please enter valid numbers.")

        elif choice == "3":
            try:
                first, second = get_numbers()
                result = multiply(first, second)
                print(f"Result: {result}")
            except ValueError:
                print("Error: Please enter valid numbers.")
        elif choice == "4":
            try:
                first, second = get_numbers()
                result = divide(first, second)
                print(f"Result: {result}")
            except ValueError as error:
                print(f"Error: {error}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()

