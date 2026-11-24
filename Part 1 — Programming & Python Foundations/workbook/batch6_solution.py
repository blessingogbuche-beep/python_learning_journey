# CREATING STRINGS[multi_line strings]

receipt = """ STORE RECEIPT
product : Laptop
Total:  ₦500,000"""
print(receipt)

print()
#Create three variables:

customer_name = "Joy"
city = "Otukpo"

product_name = "Laptop"

message = "Customer: " + customer_name +"\nCity: " + city +"\nProduct: " +product_name

print(message)

print()

#using .Format

message = """ Customer: {}
City: {}
Product: {}""".format(customer_name, city,product_name)
print(message)

print()

first = "Chris"
last = "Obi"
full_name = "First: " + first +"\nLast: " + last
print("=" * 20)
print(full_name)
print("=" * 20) 
print()

age = 25
print("Age: " + str(age))

print()

first = "Jane"
last_name = "Odoh"
full_name = "First: " + first +"\nLast: " + last_name
print("=" * 30)
print(full_name)
print("=" * 30)
full_name = "First: " + first + "\nLast: " + last_name

print()



#len()

name = "Chris"
print(len(name))

print(len("Hello World"))

print()
#indexing
 

