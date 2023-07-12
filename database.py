import random

def generate_account_number():
    return random.randint(10000000, 99999999)

database = {}
account_numbers = set()

def update_database(account_number, customer_info):
    database[account_number] = customer_info

# Check if an account number is unique
def is_unique_account_number(account_number):
    return account_number not in account_numbers

# Create a new customer account
def create_account(name, password, balance=0):
    account_number = generate_account_number()
    while not is_unique_account_number(account_number):
        account_number = generate_account_number()
    
    customer_info = {
        'name': name,
        'password': password,
        'balance': balance
    }
    update_database(account_number, customer_info)
    account_numbers.add(account_number)

    print("Account created successfully.")
    print(f"Account Number: {account_number}")

# Retrieve customer information by account number
def get_customer_info(account_number):
    return database.get(account_number, None)

# Update customer balance in the database
def update_balance(account_number, new_balance):
    if account_number in database:
        database[account_number]['balance'] = new_balance

# Reset customer password in the database
def reset_password(account_number, new_password):
    if account_number in database:
        database[account_number]['password'] = new_password

# Make a transfer between two customer accounts
def make_transfer(sender_account_number, recipient_account_number, amount):
    sender_info = get_customer_info(sender_account_number)
    recipient_info = get_customer_info(recipient_account_number)

    if not sender_info or not recipient_info:
        print("Invalid account number(s).")
        return

    sender_balance = sender_info['balance']
    recipient_balance = recipient_info['balance']

    if sender_balance < amount:
        print("Insufficient funds.")
    else:
        sender_balance -= amount
        recipient_balance += amount

        update_balance(sender_account_number, sender_balance)
        update_balance(recipient_account_number, recipient_balance)

        print("Transfer successful.")

# Close customer account
def close_account(account_number):
    if account_number in database:
        del database[account_number]
        account_numbers.remove(account_number)
        print("Account closed successfully.")
    else:
        print("Invalid account number.")
