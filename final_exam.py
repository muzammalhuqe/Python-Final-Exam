
class Bank:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.totalBalance = 0
        self.totalLoan = 0
        self.loanStatus = True
        self.accounts = []

    def createAcoount(self, name, email, address, account_type):
        account = Account(name, email, address, account_type)
        self.accounts.append(account)
        return account
        
    def deleteAccount(self, accountNumber):
        for account in self.accounts:
            if account.accountNumber == accountNumber:
                self.accounts.remove(account)
                del account
                return
        print("No Account Found To Delete")

    def showUsers(self):
        for account in self.accounts:
            print(f"Account Number : {account.accountNumber} of {account.name}")


    def showTotalBalance(self):
        print(f"Total Available Balance : {self.totalBalance}")

    def showTotalLoan(self):
        print(f"Total Loan : {self.totalLoan}")

    def onLoan(self):
        self.loanStatus = True

    def offLoan(self):
        self.loanStatus = False


class Account:
    genarateAccountNumber = 0

    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        Account.genarateAccountNumber += 1
        self.accountNumber = Account.genarateAccountNumber
        self.balance = 0
        self.loanCount = 0
        self.loanAmonut = 0
        self.transactions = []
        self.transactionId = self.accountNumber * 500

    
    def checkAvailableBalance(self):
        print(f"Name : {self.name}")
        print(f"Account Number : {self.accountNumber}")
        print(f"Balance : {self.balance}")
        

    def transfer(self, bank, targetAccNo, amount):
        for account in bank.accounts:
            if targetAccNo == account.accountNumber:
                other = account
                if self.balance >= amount:
                    self.balance -= amount
                    other.balance += amount
                    print(f"Transferred {amount} from {self.name} to {other.name}")

                    transaction = {}
                    self.transactionId += 1
                    transaction["id"] = self.transactionId
                    transaction["type"] = "transfer"
                    transaction["from"] = self.name
                    transaction["to"] = other.name
                    transaction["amount"] = amount
            
                    self.transactions.append(transaction)

                else:
                    print(f"Insufficient Amount !")
                
                return
        
        print("Account does not exist")


    def deposit(self, bank, amount):
        if amount > 0:
            bank.totalBalance += amount
            self.balance += amount

            transaction = {}
            self.transactionId += 1
            transaction["id"] = self.transactionId
            transaction["type"] = "deposit"
            transaction["amount"] = amount

            self.transactions.append(transaction)

        else:
            print("Invalid Amount")

    def withdraw(self, bank, amount):
        if amount > 0 and bank.totalBalance >= amount and self.balance >= amount:
            bank.totalBalance -= amount
            self.balance -= amount


            transaction = {}
            self.transactionId += 1
            transaction["id"] = self.transactionId
            transaction["type"] = "withdraw"
            transaction["amount"] = amount

            self.transactions.append(transaction)

        else:
            print("Withdrawal amount exceeded")

    def takeLoan(self, bank, amount):
        if bank.loanStatus == True and amount > 0 and bank.totalBalance >= amount and self.loanCount < 2:
            self.loanAmonut += amount
            self.balance += amount
            self.loanCount += 1
            bank.totalLoan += amount

            transaction = {}
            self.transactionId += 1
            transaction["id"] = self.transactionId
            transaction["type"] = "loan"
            transaction["amount"] = amount

            self.transactions.append(transaction)

        else:
            print("Invalid Loan Request")



    def showTransactionHistory(self):
        print(f"Transaction History of {self.name}:")
        
        for transaction in self.transactions:
            if "to" in transaction:
                print(f"{transaction['id']}: {transaction['type']} of taka {transaction['amount']} to {transaction['to']}")
            
            elif "id" in transaction:
                print(f"{transaction['id']}: {transaction['type']} of taka {transaction['amount']}")

bank = Bank("Prime Bank Ltd", "Rajshahi")
admin = bank.createAcoount("admin", "admin@gmail.com", "rajshahi", "admin")
user = bank.createAcoount("Muzammel", "muzammel@gmail.com", "baya","user")

currentUser = admin
changeUser = True

# currentUser = user
# changeUser = True
currentUser = None

while True:
    print("""
        1. ADMIN
        2. USER
        3. EXIT
        """)
    op = int(input("Enter your choice : "))
    if op == 1:
        print("ADMIN ID = admin,  ADMIN PASS = 123")
        id = input("Enter id : ")
        pas = input("Enter password : ")

        print("\n<------------------>")
        print("Welcome to ADMIN")
        print("<------------------>\n")

        while True:
            print()
            print("1: Create Account")
            print("2: Delete Account")
            print("3: Show Users")
            print("4: Check Total Balance")
            print("5: Check Total Loan")
            print("6: On Loan")
            print("7: Off Loan")
            print("8: Log Out")

            choice = int(input("Enter option : "))

            if choice == 1:
                name = input("Enter your name : ")
                email = input("Enter your email : ")
                address = input("Enter your address : ")
                account_type = input("Account Type (Savings/Current) : ")

                bank.createAcoount(name, email, address, account_type)
                print("Account create successful")
                
            elif choice == 2:
                accountNumber = int(input("Enter account number : "))
                bank.deleteAccount(accountNumber)
                print("Remove account successful")

            elif choice == 3:
                bank.showUsers()

            elif choice == 4:
                bank.showTotalBalance()

            elif choice == 5:
                bank.showTotalLoan()
                
            elif choice == 6:
                bank.onLoan()
                print("Loan is On")

            elif choice == 7:
                bank.offLoan()
                print("Loan is Off")

            elif choice == 8:
                break
            
            else:
                print("Invalid options")

    elif op == 2:
        while True:
            if currentUser == None:

                print("No logged in user \n")

                opson = input("Login or Register (L/R) : ")

                if opson == "R":
                    name = input("Enter your name : ")
                    email = input("Enter your email : ")
                    address = input("Enter your address : ")
                    account_type = input("Account Type (Savings/Current) : ")

                    user = bank.createAcoount(name, email, address, account_type)

                    currentUser = user
                    changeUser = True

                else:
                    id = int(input("Enter Account Number : "))

                    found = False
                    for user in bank.accounts:
                        if id == user.accountNumber:
                            currentUser = user
                            changeUser = True
                            found = True
                            break
                    if found == False:
                        print("\nUser not found\n")

                            
                    
            else:
                print(f"\nWelcome to {currentUser.name}\n")
                if currentUser.account_type == "Current":
                    # print("USER MENU")
                    print()
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Check Transaction History")
                    print("5. Take Loan")
                    print("6. Transfer")
                    print("7. Logout")
                    
                    user_choice = int(input("Enter your choice: "))

                    if user_choice == 1:
                        amount = int(input("Enter amount to deposit: "))
                        currentUser.deposit(bank, amount)
                    
                    elif user_choice == 2:
                        amount = int(input("Enter amount to withdraw: "))
                        currentUser.withdraw(bank, amount)
                    
                    elif user_choice == 3:
                        currentUser.checkAvailableBalance()
                    
                    elif user_choice == 4:
                        currentUser.showTransactionHistory()
                    
                    elif user_choice == 5:
                        amount = int(input("Enter loan amount: "))
                        currentUser.takeLoan(bank, amount)
                    
                    elif user_choice == 6:
                        target_account_number = int(input("Enter target account number for transfer: "))
                        amount = int(input("Enter amount to transfer: "))
                        currentUser.transfer(bank, target_account_number, amount)
                    
                    elif user_choice == 7:
                        currentUser = None
                        break

                    else:
                        print("Invalid choice. Please enter a valid option.")
                
                else:
                    # print("USER MENU")
                    print()
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Check Transaction History")
                    print("5. Take Loan")
                    print("6. Transfer")
                    print("7. Logout")
                    
                    user_choice = int(input("Enter your choice: "))

                    if user_choice == 1:
                        amount = int(input("Enter amount to deposit: "))
                        currentUser.deposit(bank, amount)
                    
                    elif user_choice == 2:
                        amount = int(input("Enter amount to withdraw: "))
                        currentUser.withdraw(bank, amount)
                    
                    elif user_choice == 3:
                        currentUser.checkAvailableBalance()
                    
                    elif user_choice == 4:
                        currentUser.showTransactionHistory()
                    
                    elif user_choice == 5:
                        amount = int(input("Enter loan amount: "))
                        currentUser.takeLoan(bank, amount)
                    
                    elif user_choice == 6:
                        target_account_number = int(input("Enter target account number for transfer: "))
                        amount = int(input("Enter amount to transfer: "))
                        currentUser.transfer(bank, target_account_number, amount)
                    
                    elif user_choice == 7:
                        currentUser = None
                        break

                    else:
                        print("Invalid choice. Please enter a valid option.")
    
    elif op == 3:
        break
