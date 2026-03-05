def calculate():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        total_sum = num1 + num2
        print(f"Sum: {total_sum}")

        division = num1 / num2
        print(f"Division Result: {division}")

    except ValueError:
        print("Invalid input")
    except ZeroDivisionError:
        print("Cannot divide by zero")

calculate()