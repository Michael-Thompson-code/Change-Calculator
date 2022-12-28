#I Michael Thompson, 000894336, certify that this work is my own effort and that I have not allowed anyone else to copy from it.
import random

amount: float = random.randint(0, 20) + round(random.randint(0,100) /100, 2)

print("Transaction Amount:")
print(amount)

print("Input amount paid:")
payment = input("=")

change = int(float(payment)) - amount

if change > 0:
    print("change owed:")
    print(change)

else:
    print("No change owed")

d = 1.00
q = 0.25
i = 0.10
n = 0.05

def coin_owed(change, coin_type, coin_amount):
    num_coins = 0
    while change >= coin_amount:
        num_coins += 1
        change -= coin_amount
    print(num_coins, coin_type + "(s)")
    return change

print("you got:")
temp_change = change
temp_change = coin_owed(temp_change, "dollar", d)
temp_change = coin_owed(temp_change, "quarter", q)
temp_change = coin_owed(temp_change, "dime", i)
temp_change = coin_owed(temp_change, "nickle", n)
print("back in change")


