# Program to check Armstrong numbers in a certain interval

# Function to check Armstrong numbers in a given range
def find_armstrong_numbers(lower, upper):
    # Initialize a list to store Armstrong numbers
    output = []

    # Loop through the range of numbers
    for i in range(lower, upper + 1):
        n = len(str(i))  # Find the number of digits

        split_num = list(str(i))  # Convert the number to a list of digits

        total = []

        # Calculate sum of digits raised to the power of 'n'
        for j in split_num:
            mul_num = int(j) ** n  # Raise each digit to the power of 'n'
            total.append(mul_num)

        # Check if the sum of powers is equal to the original number
        if sum(total) == i:
            output.append(i)  # Add Armstrong number to the output list

    # Return the list of Armstrong numbers
    return output

# Driver Code
lower = 100
upper = 1000

# Call the function and display Armstrong numbers in the range
armstrong_numbers = find_armstrong_numbers(lower, upper)
print("Armstrong numbers in the range:", armstrong_numbers)

