class BankAccount:
    def __init__(self, account_holder, balance): 
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f'Se ha depositado {amount}. saldo actual {self.balance}')
        else:
            print('No se puede depositar cuenta inactiva')

    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                PermissionError(f'Se ha retirado {amount}, Saldo actual {self.balance}')

    def deactivate_account(self):
        self.is_active = False
        print(f'La cuenta ha sido desactivada')

    def activate_account(self):
        self.is_active = True
        print(f'La cuenta ha sido activada')

account1 = BankAccount('Nico', 500000)
account2 = BankAccount('Alejandro', 500000)
account3 = BankAccount('Emanuel', 500000)
account4 = BankAccount('Freddy', 1000000)

# LLamada a los metodos 
account1.deposit(30000)
account2.deposit(30000)
account3.deposit(30000)
account4.deposit(60000)
account3.deactivate_account()
account3.deposit(5000)
account3.activate_account()
account3.deposit(5000)