class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit_amount(self, amount):
        self.balance += amount
        return f"Funds added to Account. Current Balance: {self.balance}" 

    def withdraw_amount(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Take your money. Current Balance: {self.balance}" 
        else:
            return "Insufficient funds." 

    def show_balance(self):
        return f"Current Balance: {self.balance}"  


account = BankAccount(1000)

while True:
    print("\n--- BANK ACCOUNT MENU ---")
    print("1. Deposit amount")
    print("2. Withdraw amount")
    print("3. Show balance")
    print("0. Exit")
    
    choice = input("Enter your choice (1-3, or 0 to exit): ")
    
    if choice == '1':
        amount = float(input("Enter the amount to deposit: "))
        print(account.deposit_amount(amount))
        
    elif choice == '2':
        amount = float(input("Enter the amount to withdraw: "))
        print(account.withdraw_amount(amount))
        
    elif choice == '3':
        print(account.show_balance())
        
    elif choice == '0':
        print("Exiting the program. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 0.")