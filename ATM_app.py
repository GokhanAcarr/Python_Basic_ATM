# We won't use any data from outside so lets create a customer

gokhanAcar = {
    "name": "Gökhan Acar",
    "balance": 3000
}

def withdraw(account, amount):
    if account["balance"] >= amount:
        account["balance"] -= amount
        print(f"Your new Balance is {account['balance']} after withdraw")
    else:
        print("Insufficient funds!")
    
def deposit(account, amount):
    account["balance"] += amount
    print(f"Your new Balance is {account['balance']} after deposit")


action = input(f"Hello {gokhanAcar['name']} Can you choose the action you want to do?(Withdraw/Deposit/BalanceInquiry)")

if action == "Withdraw":
    amount = int(input("Could you please specify how much money you want to withdraw?:"))
    withdraw(gokhanAcar, amount)
elif action == "Deposit":
    amount = int(input("Could you please specify how much money you want to deposit?:"))
    deposit(gokhanAcar, amount)
elif action == "BalanceInquiry":
     print(f"Your current balance is {gokhanAcar['balance']}")
else: 
    print("Error!")