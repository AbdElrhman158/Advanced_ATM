from ATM import ATM 
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
