import calculator
def main():
    print("\nModual 11_Module Calculator\n")
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Percentage")
        print("6. Quit\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = calculator.add(num1, num2)
            print(f"Result: {num1} + {num2} = {result:.2f}\n")
        elif choice == "2":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = calculator.sub(num1, num2)
            print(f"Result: {num1} - {num2} = {result:.2f}\n")
        elif choice == "3":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = calculator.mul(num1, num2)
            print(f"Result: {num1} * {num2} = {result:.2f}\n")
        elif choice == "4":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = calculator.div(num1, num2)
            print(f"Result: {num1} / {num2} = {result:.2f}\n")
        elif choice == "5":
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = calculator.percentage(num1, num2)
            print(f"Result: {num1} is {result:.2f}% of {num2}\n")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
