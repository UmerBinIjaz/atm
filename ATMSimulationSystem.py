user_data = {
    "user123" : {"pin": "1234", "balance": 5000.0}
}

def authenticate_user(username, pin): # Function Definition
    if username in user_data and user_data[username]["pin"] == pin:
        return True
    return False

def check_balance(username):
    print("Your current balance is: " + str(user_data[username]['balance']))

def deposite(username):
    amount = float(input("Enter the amount to deposite: "))
    
    if amount > 0:
        user_data[username]['balance'] += amount
        print("Amount deposited successfully. Your new balance is: ")
        check_balance(username)
    else:
        print("Invalid amount. Please enter a positive number.")

def withdraw(username):
    amount = float(input("Enter the amount to withdraw: "))

    if amount > 0 and amount <= user_data[username]['balance']:
        user_data[username]['balance'] -= amount
        print("Amount withdrawn successfully. Your new balance is: ")
        check_balance(username)
    else:
        print("Invalid amount. Please enter a positive number that does not exceed your balance.")

def show_menu():
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposite")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Please select an option: ")

        if choice == '1':
            check_balance(username)
        elif choice == '2':
            deposite(username)
        elif choice == '3':
            withdraw(username)
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    print("Welcome to the ATM Simulation System")
    username = input("Please enter your username: ")
    pin = input("Please enter your PIN: ")

    if authenticate_user(username, pin):
        print("Authentication successful. Welcome, " + username + "!")
        show_menu()
    else:
        print("Authentication failed. Please check your username and PIN.")