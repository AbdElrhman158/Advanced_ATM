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

class Bank_Accounts:
    def __init__(self):
        self.accounts = {}

    def create_account(self, balance):
        import random
        account_number = random.randint(1000, 9999)
        while account_number in self.accounts:
            account_number = random.randint(1000, 9999)
        new_account = ATM(balance, account_number)
        self.accounts[account_number] = new_account
        return account_number
    
    def save_accounts(accounts):
    # Open the file in write mode
        file = open("accounts.txt", "w")
    # Loop through the accounts list and write each account's information to the file
        for account in accounts:
            file.write(f"{account.account_number},{account.balance},\n")
    # Close the file
        file.close()
    

    def login(self, account_number):
        if isinstance(account_number, int) and account_number in self.accounts:
   
            return self.accounts[account_number]
        else:
            return None 
    def operate(self, atm):
        print(f"Welcome to your account {atm.account_number}")
        while True:
            print("Please choose an option:")
            print("1. Check balance")
            print("2. Deposit money")
            print("3. Withdraw money")
            print("4. Transfer money")
            print("5. Print transaction history")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice in ["1", "2", "3", "4", "5", "6"]:
                choice = int(choice)
                if choice == 1:
                    balance = atm.check_balance()
                    print(f"Your current balance is {balance}")
                elif choice == 2:
                    amount = float(input("Enter the amount to deposit: "))
                    result = atm.deposit(amount)
                    if result:
                        print(f"Successfully deposited {amount}")
                    else:
                        print(f"Invalid amount")
                elif choice == 3:
                    amount = float(input("Enter the amount to withdraw: "))
                    result = atm.withdraw(amount)
                    if result:
                        print(f"Successfully withdrew {amount}")
                    else:
                        print(f"Invalid amount or insufficient balance")
                elif choice == 4:
                    amount = float(input("Enter the amount to transfer: "))
                    other_account_number = int(input("Enter the other account number: "))
                    if other_account_number in self.accounts:
                        other_account = self.accounts[other_account_number]
                        result = atm.transfer(amount, other_account)
                        if result:
                            print(f"Successfully transferred {amount} to account {other_account_number}")
                        else:
                            print(f"Invalid amount or insufficient balance")
                    else:
                        print(f"Invalid account number")
                elif choice == 5:
                    atm.print_history()
                elif choice == 6:

                    break
            
            else:

                print("Invalid choice. Please enter a number between 1 and 6.")

            print()

        print(f"Thank you for using your account {atm.account_number}")


bank=Bank_Accounts()
while True:
    choice = input("Enter your choice: ")

    if choice in ["1", "2", "3"]:
        choice = int(choice)     
        if choice == 1: 
            balance = float(input("Enter your initial balance: "))
            account_number = bank.create_account(balance)
            print(f"Your new account number is {account_number}")
        elif choice == 2:
            account_number = int(input("Enter your account number: "))
            atm = bank.login(account_number)
            if atm is not None:
                bank.operate(atm)
            else:
                print(f"Invalid account number")
        elif choice == 3:
            print("Have a nice day :)")
            break

    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

print()