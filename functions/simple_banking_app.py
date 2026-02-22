"""
create a simple banking application with deposit, withdrawal, check balance
"""
balance = 0
def check_kyc():
    pass
def update_kyc():
    pass

def check_balance():
    print(f"Your account Balance is Rs{balance}")
    print("===================================")
    print()


def amount_deposit(amount):
    global balance
    if amount >= 0:
        balance += amount
        print(f"You have deposited Rs{amount} to your Bank account Successfully")
        print(f"Your Account balance is:Rs{balance}")
        print("===================================")
        print()
    elif amount < 0:
        print("You cannot deposit negative amount! Please enter a correct Amount to deposit")
        print("===================================")
        print()
    else:
        print(f"You have entered an Invalid Input")
        print(f"Your Account balance is:Rs{balance}")
        print("===================================")
        print()

def amount_withdraw(amount):
    global balance
    if amount <= 0:
        print("You cannot withdraw negative/Zero amount! Please Try again!")
        print("===================================")
        print()
    elif amount > balance:
        print("You account does not have sufficient Balance! Please Try with less amount Than account Balance!")
        print(f"Your Account balance is:Rs{balance}")
        print("===================================")
        print()
    else:
        balance -= amount
        print(f"You have account has been debited with amount Rs:{amount} Successfully")
        print(f"Your Account balance is:Rs{balance}")
        print("===================================")
        print()

if __name__ == '__main__':
    print("===================================")
    print("Welcome to PSF Bank")
    print("===================================")
    print()
    while True:
        print("1.Check your Balance")
        print("2.Deposit Amount")
        print("3.Withdraw Amount")
        print("4.Check your KYC status")
        print("5.Update your KYC")
        print("6.Quit")
        print()
        choice = input("Enter your choice (1-6):")
        if choice == "1":
            check_balance()
        elif choice == "2":
            while True:
                try:
                    amt=float(input("Enter the amount you want to Deposit to your Bank account:Rs "))
                    amt=float(amt)
                    amount_deposit(amt)
                    break
                except ValueError:
                    print("Error: That is not a valid amount. Please try again.")
        elif choice == "3":
            while True:
                try:
                    amt=float(input("Enter the amount you want to Withdraw from your Bank account:Rs "))
                    amt=float(amt)
                    amount_withdraw(amt)
                    break
                except ValueError:
                    print("Error: That is not a valid amount. Please try again.")

        elif choice == "6":
            break
        else:
            print("Invalid Input !! Retry with Correct choice.")
            print()
            # continue

    print()
    print("===================================")
    print("Thank you for Banking with PSF Bank!!\nYou have a Good Day!!")


