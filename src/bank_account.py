class BankAccount:

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сума для депозиту повинна бути більшою за 0.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сума для зняття повинна бути більшою за 0.")
        if amount > self.balance:
            raise ValueError("Недостатньо коштів на рахунку.")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

# Приклад використання
if __name__ == "__main__":
    account = BankAccount("Іван Іванов", 1000)
    print("Початковий баланс:", account.get_balance())
    account.deposit(500)
    print("Після депозиту:", account.get_balance())
    account.withdraw(300)
    print("Після зняття:", account.get_balance())
