class BankAccount:
    def __init__(self, account_number, initial_balance = 0):
        self.__account_number = account_number
        self.__balance = initial_balance

    def Deposite(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Deposite: Rs.{amount}. New Balance: Rs.{self.__balance}')
        else:
            print('Deposite amount must be positive')
    
    def Withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f'Withdraw: Rs.{amount}. New Balance: Rs.{self.__balance}')
            else:
                print('Insuficent Balance')
        else:
            print('Withdraw amount must be positive')
    
    def get_balance(self):
        return self.__balance
    
    def get_account_number(self):
        return self.__account_number

bank = BankAccount('12345', 1000)
print(f'Current Balance: Rs.{bank.get_balance()}')
bank.Deposite(500)
bank.Withdraw(300)