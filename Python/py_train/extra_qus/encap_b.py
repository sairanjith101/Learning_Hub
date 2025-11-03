class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number  # Private attribute for account number
        self.__balance = initial_balance  # Private attribute for balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrew: ${amount}. New balance: ${self.__balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    # Method to get current balance (if needed)
    def get_balance(self):
        return self.__balance

    # Method to get account number (if needed)
    def get_account_number(self):
        return self.__account_number


# Example usage:

account = BankAccount("12345678", 1000)

# Deposit
account.deposit(500)

# Withdraw
account.withdraw(200)

# Check balance
print(f"Current balance: ${account.get_balance()}")
