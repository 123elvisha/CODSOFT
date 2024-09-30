class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return int(self.num1 + self.num2)

    def subtract(self):
        return int(self.num1 - self.num2)

    def multiply(self):
        return int(self.num1 * self.num2)

    def divide(self):
        if self.num2 != 0:
            return int(self.num1 / self.num2)
        else:
            return "Error: Division by zero!"

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    calculator = Calculator(num1, num2)

    while True:
        print("Select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = int(input("Enter your choice (1/2/3/4/5): "))

        if choice == 1:
            result = calculator.add()
        elif choice == 2:
            result = calculator.subtract()
        elif choice == 3:
            result = calculator.multiply()
        elif choice == 4:
            result = calculator.divide()
        elif choice == 5:
            print("Thank you!")
            break
        else:
            print("Invalid choice. Try again!")
            continue

        if isinstance(result, int):
            print(f"Result: {result}")
        else:
            print(result)

if __name__ == "__main__":
    main()