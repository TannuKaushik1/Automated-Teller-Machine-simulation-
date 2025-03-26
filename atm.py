import datetime

# Sample data: Dictionary to store account information
accounts = {
    '1234567890': {'pin': '1234', 'balance': 1500.00, 'transaction_history': []},
    '0987654321': {'pin': '4321', 'balance': 200.00, 'transaction_history': []}
}

# Function to check if account exists
def account_exists(account_number):
    return account_number in accounts

# Function to check PIN
def check_pin(account_number, pin):
    return accounts[account_number]['pin'] == pin

# Function for account balance inquiry
def check_balance(account_number):
    return accounts[account_number]['balance']

# Function for cash withdrawal
def withdraw(account_number, amount):
    if accounts[account_number]['balance'] >= amount:
        accounts[account_number]['balance'] -= amount
        transaction = {'type': 'Withdrawal', 'amount': amount, 'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        accounts[account_number]['transaction_history'].append(transaction)
        return True, "Transaction successful. Please take your cash."
    else:
        return False, "Insufficient balance."

# Function for cash deposit
def deposit(account_number, amount):
    accounts[account_number]['balance'] += amount
    transaction = {'type': 'Deposit', 'amount': amount, 'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    accounts[account_number]['transaction_history'].append(transaction)
    return "Deposit successful. Thank you for banking with us."

# Function for PIN change
def change_pin(account_number, current_pin, new_pin):
    if check_pin(account_number, current_pin):
        accounts[account_number]['pin'] = new_pin
        return True, "PIN successfully changed."
    else:
        return False, "Invalid current PIN. Please try again."

# Function for transaction history
def get_transaction_history(account_number):
    return accounts[account_number]['transaction_history']

# Main program loop
def main():
    while True:
        print("\nWelcome to the ATM")
        account_number = input("Enter your account number: ")
        
        if account_exists(account_number):
            pin = input("Enter your PIN: ")
            
            if check_pin(account_number, pin):
                while True:
                    print("\nPlease select an option:")
                    print("1. Check Balance")
                    print("2. Withdraw Cash")
                    print("3. Deposit Cash")
                    print("4. Change PIN")
                    print("5. Transaction History")
                    print("6. Exit")
                    
                    choice = input("Enter your choice (1-6): ")
                    
                    if choice == '1':
                        balance = check_balance(account_number)
                        print(f"Your account balance is ${balance:.2f}")
                    elif choice == '2':
                        amount = float(input("Enter amount to withdraw: "))
                        success, message = withdraw(account_number, amount)
                        print(message)
                    elif choice == '3':
                        amount = float(input("Enter amount to deposit: "))
                        message = deposit(account_number, amount)
                        print(message)
                    elif choice == '4':
                        new_pin = input("Enter new PIN: ")
                        success, message = change_pin(account_number, pin, new_pin)
                        print(message)
                    elif choice == '5':
                        history = get_transaction_history(account_number)
                        print("\nTransaction History:")
                        for transaction in history:
                            print(f"{transaction['date']} - {transaction['type']} of ${transaction['amount']:.2f}")
                    elif choice == '6':
                        print("Thank you for using the ATM. Goodbye!")
                        break
                    else:
                        print("Invalid choice. Please enter a number between 1 and 6.")
            
            else:
                print("Invalid PIN. Please try again.")
        
        else:
            print("Account number not found. Please try again.")

if _name_ == "_main_":
    main()