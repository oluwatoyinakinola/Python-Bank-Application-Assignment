import database

def deposit_money():
    customer_account_number = int(input("Enter the customer's account number: "))
    amount = float(input("Enter the amount to deposit: "))

    customer_info = database.get_customer_info(customer_account_number)

    if customer_info:
        new_balance = customer_info['balance'] + amount
        database.update_balance(customer_account_number, new_balance)
        print("Deposit successful")
    else:
        print("Invalid account number")

def reset_customer_password():
    customer_account_number = int(input("Enter the customer's account number: "))
    new_password = input("Enter the new password: ")

    customer_info = database.get_customer_info(customer_account_number)

    if customer_info:
        database.reset_password(customer_account_number, new_password)
        print("Customer password reset successful.")
    else:
        print("Invalid account number.")

# Run the agent actions
def agent_actions():
    while True:
        print("\nAgent Actions:")
        print("1. Deposit money into customer's account")
        print("2. Reset customer's password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            deposit_money()
        elif choice == "2":
            reset_customer_password()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

# Execute agent actions
agent_actions()
