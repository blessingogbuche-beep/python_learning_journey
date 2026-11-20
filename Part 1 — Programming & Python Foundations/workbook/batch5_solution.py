#Printing multiple values
name = "Chris"
balance = 50000

print(name, balance)

print()

product_name = "Laptop"
price = 250000
quantity = 2
balance = price * quantity

print(product_name)
print(price)
print(quantity)
print(balance)


#print("Total:", total)

print()
#SEPARATING VALUES
print("Wallet", "Balance", 50000)
print()

print("Wallet", "Balance", 50000, sep=" | ")

print()

print("Hello")
print("World")

print()

print("Hello", end=" ")
print("World")

print()
#INPUT — input()
#python wait for you to input name
name = input()

#ADDING A PROMPT
name = input("Enter your name: ")

print()
name = input("Enter your name: ")
print("Hello", name)

print()

age = input("Enter your age: ")

print()


#WALLET INPUT
balance = float(input("Enter current balance: "))
deposit = float(input("Enter deposit amount: "))
balance += deposit
print("New balance:", balance)

print()

#STRING OUTPUT WITH F-STRINGS
print(f"Balance: {balance}")

name = "Chris"
balance = 50000
print(f"{name}has a balance of {balance}")

balance = 50000.50
print(f"{balance:.2f}")
print()

balance = 5000000.5
print(f"{balance:,.2f}")

print()
balance = 1250000.75
print(f"{balance:,.2f}")

print()

product_name = (input("Enter product_name: "))
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
discount = float(input("Enter discount:"))

subtotal = price * quantity
total = subtotal - discount
print()

print(f"""======================
    STORE RECEIPT
=======================""")
print(f"Product: {product_name}")
print(f"Price: ₦{price:,.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ₦{subtotal:,.2f}")
print(f"Discount: ₦{discount:,.2f}")
print(f"Total: ₦{total:,.2f}")

print("=======================")
print()

#Wallet balance ,hard challenge

customer_name = input("Enter customer_name: ")
wallet_balance = float(input("Enter wallet_balance: "))
product_price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
discount = float(input("Enter discount: "))

subtotal = product_price * quantity
total = subtotal - discount
remaining_balance =  wallet_balance - total

print(f"Name: {customer_name}")
print(f"wallet_balance: ₦{wallet_balance:,.2f}")
print(f"Product_price: ₦{product_price:,.2f}")
print(f"Quantity: {quantity:,.2f}")
print(f"Discount: ₦{discount:,.2f}")

print(f"Subtotal: ₦{subtotal:,.2f}")
print(f"Total: ₦{total:,.2f}" )
print(f"Remaining_balance: ₦{remaining_balance:,.2f}")


