import random  #module untuk mengacak nomor yang sudah di pilih
 
class Account:
    # Construct an Account object
    def __init__(self, id, balance = 0):
        self.id = id
        self.balance = balance
 
    def getId(self):
        return self.id
 
    def getBalance(self):
        return self.balance
 
    def withdraw(self, amount):
        self.balance -= amount
 
    def deposit(self, amount):
        self.balance += amount

def main():
   # Creating accounts
   accounts = []
   for i in range(1000, 9999):
       account = Account(i, 0)
       accounts.append(account)
	 # ATM Processes
   while True:
 
       # Reading id from user
       id = int(input("\nEnter account pin: "))
 
       # Loop till id is valid
       while id < 1000 or id > 9999:
           id = int(input("\nInvalid Id.. Re-enter: "))
 
       # Iterating over account session
       while True:
 
           # Printing menu
           print("\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit ")
 
           # Reading selection
           selection = int(input("\nEnter your selection: "))
 
           # Getting account object
           for acc in accounts:
               # Comparing account id
               if acc.getId() == id:
                   accountObj = acc
                   break
 
           # View Balance
           if selection == 1:
               # Printing balance
               print(accountObj.getBalance())
 
           # Withdraw
           elif selection == 2:
               # Reading amount
               amt = float(input("\nEnter amount to withdraw: "))
               ver_withdraw = input("Is this the correct amount, yes or No ? " + str(amt) + " ")
 
               if ver_withdraw == "yes":
                   print("Verify withdraw")
               else:
                   print("ketik dengan benar")
                   ver_withdraw = input("Is this the correct amount, yes or No ? " + str(amt) + " ")
 
               if amt < accountObj.getBalance():
                  # Calling withdraw method
                  accountObj.withdraw(amt)
                  # Printing updated balance
                  print("\nUpdated Balance: " + str(accountObj.getBalance()) + " ")
               else:
                    print("\nYou're balance is less than withdrawl amount: " + str(accountObj.getBalance()) + " ")
                    print("\nPlease make a deposit.")#;
 
           # Deposit
           elif selection == 3:
               # Reading amount
               amt = float(input("\nEnter amount to deposit: "))
               ver_deposit = input("Is this the correct amount, yes, or No ? " + str(amt) + " ")
 
               if ver_deposit == "yes":
                  # Calling deposit method
                  accountObj.deposit(amt)#;
                  # Printing updated balance
                  print("\nUpdated Balance: " + str(accountObj.getBalance()) + " ")
               else:
                   print("ketik dengan benar")
                   ver_deposit = input("Is this the correct amount, yes, or No ? " + str(amt) + " ")
 
           elif selection == 4:
               print("nTransaction is now complete.")
               print("Transaction number: ", random.randint(10000, 1000000))
               print("Thanks for choosing us as your bank")
               exit()
 
           # Any other choice
           else:
               print("nThat's an invalid choice.")
 
# Main function
main()