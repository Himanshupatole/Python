def is_armstrong(num):
    power = len(str(num))  # Get number of digits
    temp, armstrong_sum = num, 0
    
    while temp > 0:
        digit = temp % 10  # Extract last digit
        armstrong_sum += digit ** power  # Add digit^power to sum
        temp //= 10  # Remove last digit

    return armstrong_sum == num

# Example usage
num = int(input("Enter a number: "))
print(f"{num} is an Armstrong number" if is_armstrong(num) else f"{num} is not an Armstrong number")
