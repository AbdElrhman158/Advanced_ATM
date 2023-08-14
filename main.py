from Bank import Bank_Accounts
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