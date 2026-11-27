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

text = "Hi Joy"
print(len(text))   
print(text[2])     
print(text[3])  

print()
name = input("Enter your name: ")
#print(name[0])
print(len(name))
print(name[-1])

# """How to read [::-1] - [start:stop:step] 
# Empty start with a negative step means "begin at the last letter".
# Empty stop with a negative step means "go all the way to the first letter".
# Step -1 means "move one letter backward each time". """

print(name[::-1])

print()

#Last 3 letters, backwards	name[-1:-4:-1]	gni
# start = -1: begin at the last letter, g.
# stop = -4: stop when you reach index -4 (the second s). The stop position is not included.
# step = -1: move one letter backward each time.
print(name[-1:-4-1])

print()
# print 3 letters reversed
# start = 2: begin at index 2, the letter e. The start is included.
# stop = empty: with a negative step, an empty stop means "keep going until the first letter".
# step = -1: move one letter backward each time.


name = "blessing"
print(name[2::-1])

print()

#Every second letter from the end name[::-2] "gisl"

name = "Blessing"
print(name[::-2])
print()

#when :: means no boundary for a stop.
#name = "Blessing"
# print(name[2:])     essing  (no stop, so it goes to the end, g included)
# print(name[:3])     Ble     (no start, so it begins at B; stop 3 is not included)
# print(name[::2])   Besn    (whole string, every second letter)

#  PRACTICE 5

# ```python
phone = "08012345678"
# ```

# Use slicing to print:

# ```text
# The first 4 digits
# The last 4 digits
# The middle section

print(phone[:4:])
print(phone[7::])
print(phone[4:7])

 #STRING METHODS
 #A method is a built-in action that belongs to a string. You write
 # the string, then a dot, then the method name with round brackets:
 
text = "  Hello World  "
print(text.upper())
print(text.lower())
print(text.strip())
print(text.title())

print()

name = "chris obi"
print(name.title())
print(name.replace("obi", "eze"))
print(name.count("i"))
print(name.find("o"))
print(name.startswith("chris"))
print(name.endswith("obi"))

name = "  chris  "
name.strip()
print(name)

print()
name = name.strip()
print(name)

print()

name = input("Enter your name: ").strip().title()

 #CHECKING TEXT (BOOLEAN RESULTS)

email = "chris@gmail.com"
print("@"in email)
print("gmail" in email)
print(email.endswith(".com"))
print(email.startswith("chris"))

"12345".isdigit()
"abc".isalpha()
"abc".isdigit()
print()

#f-STRING FORMATTING (REVIEW + STRETCH)
print(f"{'Item':<10}{'Price':>10}")
print(f"{'Laptop':<10}{250000:>10,}")
# Code	Meaning
# <10	left-align in 10 characters
# >10	right-align in 10 characters
# ^10	centre in 10 characters
print()

name = "chris"
print("Hello" + name + "!")

name = "chris"
balance = 500000
print(f"{name} has ₦{balance:,.2f}")