class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn. New balance: ₹{self.balance}")
        else:
            print("Insufficient funds or invalid amount!")

# Example usage
account = Account("Alice", 5000)
account.deposit(2000)
account.withdraw(3000)
account.withdraw(5000)  # Should show an error message
