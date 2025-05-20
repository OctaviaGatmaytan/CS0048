import sys

def calculator():
    while True:
        # Display Menu
        print("\n-- Menu --")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 5.")
            continue

        if choice == 5:
            print("Exiting... Goodbye!")
            sys.exit()

        if choice in [1, 2, 3, 4]:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid number. Please enter numeric values.")
                continue

            if choice == 1:
                result = round(num1 + num2, 2)
                print(f"Result: {result}")
            elif choice == 2:
                result = round(num1 - num2, 2)
                print(f"Result: {result}")
            elif choice == 3:
                result = round(num1 * num2, 2)
                print(f"Result: {result}")
            elif choice == 4:
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                else:
                    result = round(num1 / num2, 2)
                    print(f"Result: {result}")
        else:
            print(f"{choice} is not a valid option. Please choose between 1 and 5.")

if __name__ == "__main__":
    calculator()
