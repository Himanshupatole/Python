import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
num = int(input("Enter a number: "))
print(f"{num} is Prime" if is_prime(num) else f"{num} is Not Prime")
