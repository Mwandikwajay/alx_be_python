import sys
from bank_account import BankAccount

def main():
    # Create a bank account with an initial balance of 100
    account = BankAccount(100)
    
    # Ensure that command-line arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Extract the command and optional parameters
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Handle the different banking commands
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
