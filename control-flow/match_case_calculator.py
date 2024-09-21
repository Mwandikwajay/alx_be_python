# match_case_calculator.py

# Function to perform the calculation
def calculate(num1, num2, operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            else:
                return num1 / num2
        case _:
            return "Error: Invalid operation."

# Get user input for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Get user input for operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation
result = calculate(num1, num2, operation)

# Display the result
print(f"The result is: {result}")
