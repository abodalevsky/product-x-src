# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Main program
if __name__ == "__main__":
    # Taking input from the user
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    # Calculating the sum
    result = add_numbers(number1, number2)

    # Displaying the result
    print(f"The sum of {number1} and {number2} is {result}")