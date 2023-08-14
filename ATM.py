class ATM:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number
        self.history = [] # A list to store the transaction history
    
    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited {amount} to account {self.account_number}")
            return True 
        else:
            return False 

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrew {amount} from account {self.account_number}")
            return True 
        else:
            return False 

    def transfer(self, amount, other_account):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            self.history.append(f"Transferred {amount} from account {self.account_number} to account {other_account.account_number}")
            other_account.history.append(f"Received {amount} from account {self.account_number} to account {other_account.account_number}")
            return True 
        else:
            return False 

    def print_history(self):
        print(f"Transaction history for account {self.account_number}:")
        for transaction in self.history:
            print(transaction)
