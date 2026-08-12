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
            print("Add selected")
        elif choice == "2":
            print("Subtract selected")
        elif choice == "3":
            print("Multiply selected")
        elif choice == "4":
            print("Divide selected")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()

