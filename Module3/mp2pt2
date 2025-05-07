import sys

def celsius_to_fahrenheit(celsius):
    return round((celsius * 9/5) + 32, 2)

def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 5/9, 2)

def main():
    while True:
        print("\n-- Menu --")
        print("1. Convert Fahrenheit to Celsius")
        print("2. Convert Celsius to Fahrenheit")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 3.")
            continue

        if choice == 1:
            try:
                temp = float(input("Enter temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(temp)
                print(f"Temperature in Celsius: {celsius}°C")
            except ValueError:
                print("Invalid temperature. Please enter a numeric value.")
        
        elif choice == 2:
            try:
                temp = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(temp)
                print(f"Temperature in Fahrenheit: {fahrenheit}°F")
            except ValueError:
                print("Invalid temperature. Please enter a numeric value.")
        
        elif choice == 3:
            print("Exiting... Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
