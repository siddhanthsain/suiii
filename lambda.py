# Define a lambda function to calculate the factorial of a number
factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

# Get user input for the number
num = int(input("Enter a number: "))

# Calculate the factorial using the lambda function
result = factorial(num)

# Print the result
print(f"The factorial of {num} is {result}")
