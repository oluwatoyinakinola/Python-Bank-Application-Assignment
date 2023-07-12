import database

def create_account():
    name = input("Enter your name: ")
    password = input("Enter a password: ")
    balance = float(input("Enter the initial balance: "))
    
    database.create_account(name, password, balance)

def view_account_info():
    account_number = int(input("Enter your account number: "))
    
    customer_info = database.get_customer_info(account_number)
    if customer_info:
        print(f"Name: {customer_info['name']}")
        print(f"Balance: {customer_info['balance']}")
    else:
        print("Invalid account number.")

def make_transfer():
    sender_account_number = int(input("Enter your account number: "))
    recipient_account_number = int(input("Enter recipient's account number: "))
    amount = float(input("Enter the amount to transfer: "))
    
    database.make_transfer(sender_account_number, recipient_account_number, amount)

def reset_password():
    account_number = int(input("Enter your account number: "))
    customer_info = database.get_customer_info(account_number)
    
    if customer_info:
        old_password = input("Enter old password: ")
        
        if old_password == customer_info['password']:
            reset_option = input("Do you remember your old password? (y/n): ")
            
            if reset_option == 'y':
                new_password = input("Enter new password: ")
                database.reset_password(account_number, new_password)
                
                print("Password reset successful.")
            else:
                remaining_name = input("Enter the remaining part of your name: ")
                
                if remaining_name == customer_info['name'][-len(remaining_name):]:
                    new_password = input("Enter new password: ")
                    database.reset_password(account_number, new_password)
                    
                    print("Password reset successful.")
                else:
                    print("Invalid remaining name.")
        else:
            print("Invalid old password.")
    else:
        print("Invalid account number.")

# Run the customer actions
def customer_actions():
    while True:
        print("\nCustomer Actions:")
        print("1. Create account")
        print("2. View account information")
        print("3. Make a transfer")
        print("4. Reset password")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_account()
        elif choice == "2":
            view_account_info()
        elif choice == "3":
            make_transfer()
        elif choice == "4":
            reset_password()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

# Execute customer actions
customer_actions()
