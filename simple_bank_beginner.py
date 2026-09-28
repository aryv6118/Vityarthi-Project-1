accounts = []
transactions = []

def find_account(number):
    for a in accounts:
        if a["number"] == number:
            return a
    return None

def create_account():
    name = input("Name: ")
    age = int(input("Age: "))
    balance = float(input("Opening balance: "))
    number = 1001 + len(accounts)
    accounts.append({"number": number, "name": name,
                     "age": age, "balance": balance})
    print("Account created. Number:", number)

def deposit():
    number = int(input("Account number: "))
    a = find_account(number)
    if a is None:
        print("Account not found."); return
    amount = float(input("Deposit amount: "))
    if amount <= 0:
        print("Invalid amount."); return
    a["balance"] += amount
    transactions.append((number, "Deposit", amount))
    print("Deposit successful.")

def withdraw():
    number = int(input("Account number: "))
    a = find_account(number)
    if a is None:
        print("Account not found."); return
    amount = float(input("Withdrawal amount: "))
    if amount <= 0:
        print("Invalid amount.")
    elif amount > a["balance"]:
        print("Insufficient balance.")
    else:
        a["balance"] -= amount
        transactions.append((number, "Withdrawal", amount))
        print("Withdrawal successful.")

def show_account():
    number = int(input("Account number: "))
    a = find_account(number)
    if a is None:
        print("Account not found.")
    else:
        print("Number:", a["number"])
        print("Name:", a["name"])
        print("Age:", a["age"])
        print("Balance: Rs.", a["balance"])

def show_all():
    if not accounts:
        print("No accounts.")
        return
    for a in accounts:
        print(a["number"], "-", a["name"], "- Rs.", a["balance"])

def transfer():
    sender = int(input("Sender account: "))
    receiver = int(input("Receiver account: "))
    a, b = find_account(sender), find_account(receiver)
    if a is None or b is None:
        print("Account not found."); return
    amount = float(input("Transfer amount: "))
    if amount <= 0 or amount > a["balance"]:
        print("Invalid amount or insufficient balance."); return
    a["balance"] -= amount
    b["balance"] += amount
    transactions.append((sender, "Transfer", amount))
    print("Transfer successful.")

def statistics():
    if not accounts:
        print("No accounts."); return
    balances = [a["balance"] for a in accounts]
    total = 0
    maximum = balances[0]
    for value in balances:
        total += value
        if value > maximum:
            maximum = value
    print("Total money:", total)
    print("Highest balance:", maximum)
    print("Average balance:", total / len(balances))


def collections_demo():
    numbers = [a["number"] for a in accounts]  # List
    print("List:", numbers)
    if accounts:
        print("Tuple:", (accounts[0]["number"], accounts[0]["name"]))
        print("Dictionary:", accounts[0])
    print("Set:", set(numbers))

def main():
    while True:
        print("\n===== BANK MANAGEMENT SYSTEM =====")
        print("1.Create\n2.Deposit\n3.Withdraw\n4.Transfer\n5.Show Account\n6.Show All\n7.Statistics\n8.Collections\n9.Exit")
        choice = input("Choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            transfer()
        elif choice == "5":
            show_account()
        elif choice == "6":
            show_all()
        elif choice == "7":
            statistics()
        elif choice == "8":
            collections_demo()
        elif choice == "9":
            print("Thank you!")
            break
        else:
            print("Invalid choice.")

main()