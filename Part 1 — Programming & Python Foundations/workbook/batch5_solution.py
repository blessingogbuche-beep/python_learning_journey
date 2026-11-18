#Printing multiple values

name = "chris"
balance = 50000
print(name, balance)

print()

product_name = "Laptop"
price = 250000
quantity = 2

balance = price * quantity
print("product_name:", product_name)

print("Price:", price)
print("Quantity:", quantity)
print("Balance:", balance)

print()

#SEPARATING VALUES

print("Wallet", "Ballance", 50000, sep=" | ")

print("Hello", end=" ")
print("World")

print()

print("Hello", end=" ")
print("Mr Josh", end=" ")
print("how  are you doing?")

print()

# INPUT — input()


name = input("Enter your name:")
age = input("Enter your age:")

#THE FLOW

age = int(input("Enter your age:"))
print("your age is:", age)
print(type(age))

print()

# INPUT + OPERATORS
price = int(input("Enter price: "))
quantity = int(input("Enter quantity: "))
subtotal = price * quantity
print("Subtotal:", subtotal)

#WALLET INPUT

balance = float(input("Enter current balance: "))
deposite = float(input("Enter deposite amount: "))

balance += deposite

# INPUT + CALCULATION
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
discount = float(input("Enter discount:"))

subtotal = price * quantity
total = subtotal - discount

print("Subtotal:", subtotal)
print("Total:", total)

product_name = (input("Enter product_name: "))
price = float(input("Enter price:"))
quantity = int(input("Enter quantity: "))
discount = int(input("Enter discount: "))

subtotal = price * quantity
total = subtotal - discount

print("Product:", product_name)
print("Subtotal:", subtotal)
print("Discount:", discount)
print("Total:", total)


#STRING OUTPUT WITH F-STRINGS









