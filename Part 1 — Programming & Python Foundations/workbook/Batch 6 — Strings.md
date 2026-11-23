# 🐍 PYTHON JOURNEY — BATCH 6

## Part 1 — Python Foundations

### Topic: **Strings**

> 😎 Alright, apprentice.
>
> You've now learned how to:
>
> **store data → manipulate numbers → receive data → display data.**
>
> But so far, text has mostly been something you *print*.
>
> Real programs *work* with text:
>
> * cleaning a customer's name
> * building a receipt header
> * creating a username
> * checking what an email looks like
>
> Welcome to **Strings.** 🐍⚔️

---

# 🎯 BATCH 6 MISSION

By the end of this batch, you should understand:

* What a string is
* Single, double, and triple quotes
* Escape characters (`\n`, `\t`)
* Concatenation and repetition
* `len()`
* Indexing
* Slicing
* String methods
* Strings are immutable
* Converting between numbers and strings
* Boolean results from strings
* Building text features for your Wallet App
* Building text features for your Terminal Store

---

# 🗺️ WHERE YOU ARE

```text
PART 1 — PYTHON FOUNDATIONS

[✅] Batch 1 — Programming & Python Basics
[✅] Batch 2 — Core Python Foundations
[✅] Batch 3 — Variables & Assignment
[✅] Batch 4 — Operators & Expressions
[✅] Batch 5 — Input & Output
[🔥] Batch 6 — Strings
[🔒] Batch 7 — Conditionals
[🔒] Batch 8 — Loops
```

---

# 🧠 THE BIG IDEA

A **string** is a sequence of characters.

```python
name = "Chris"
```

Think of it like a row of boxes, one character per box:

```text
 C   h   r   i   s
[0] [1] [2] [3] [4]
```

Everything in this batch comes from that picture: you can **count** the boxes, **pick** one, **cut out** a section, or **transform** the whole row.

---

# 1️⃣ CREATING STRINGS

```python
name = "Chris"
city = 'Lagos'
```

Both quote styles work. Pick one and stay consistent.

## Quotes inside quotes

```python
message = "It's a good day"
quote = 'He said "hello"'
```

## Multi-line strings

```python
receipt = """STORE RECEIPT
Product: Laptop
Total: ₦500,000"""

print(receipt)
```

---

# ⚠️ STRINGS VS NUMBERS

```python
print(5 + 5)       # 10
print("5" + "5")   # 55
```

`5` is a number. `"5"` is text. They behave differently.

You already know this from `input()`: it always returns a string, which is why you used `float()` and `int()`.

---

# 🧪 PRACTICE 1

Create three variables:

```text
customer_name
city
product_name
```

Print each one. Then print a multi-line string that contains all three.

---

# 2️⃣ ESCAPE CHARACTERS

Some characters need special codes.

```python
print("Line one\nLine two")
print("Name:\tChris")
print("She said \"hi\"")
```

| Code | Meaning |
|---|---|
| `\n` | new line |
| `\t` | tab |
| `\"` | a double quote |
| `\\` | a backslash |

---

# 🧪 PRACTICE 2

Print a three-line receipt using only **one** `print()` and `\n`.

---

# 3️⃣ JOINING AND REPEATING

## Concatenation (`+`)

```python
first = "Chris"
last = "Obi"

full_name = first + " " + last
print(full_name)
```

You must add the space yourself.

## Repetition (`*`)

```python
print("=" * 20)
print("-" * 20)
```

Great for receipt borders.

## ⚠️ Common error

```python
age = 25
print("Age: " + age)     # TypeError
```

Fix with `str()` or an f-string:

```python
print("Age: " + str(age))
print(f"Age: {age}")
```

---

# 🧪 PRACTICE 3

Ask for first and last name. Build `full_name` with `+`, then print it between two lines of `"=" * 30`.

---

# 4️⃣ `len()`

```python
name = "Chris"
print(len(name))     # 5
```

`len()` counts characters, **including spaces**.

```python
print(len("Hello World"))   # 11
```

---

# 5️⃣ INDEXING

Positions start at **0**.

```python
word = "Python"

print(word[0])    # P
print(word[1])    # y
print(word[5])    # n
```

Negative numbers count from the end:

```python
print(word[-1])   # n
print(word[-2])   # o
```

## ⚠️ Index out of range

```python
print(word[10])   # IndexError
```

The last valid index is always `len(word) - 1`.

---

# 🧪 PRACTICE 4

Ask for a name. Print:

```text
First letter
Last letter
Length
```

---

# 6️⃣ SLICING

Syntax:

```python
text[start:stop]
```

`start` is **included**. `stop` is **not**.

```python
word = "Python"

print(word[0:2])    # Py
print(word[2:5])    # tho
print(word[:3])     # Pyt   (from the start)
print(word[3:])     # hon   (to the end)
print(word[-3:])    # hon   (last three)
print(word[:])      # Python
```

Mental model:

```text
 P   y   t   h   o   n
 0   1   2   3   4   5   6
 ↑                       ↑
start                  stop positions sit BETWEEN characters
```

---

# 🧪 PRACTICE 5

```python
phone = "08012345678"
```

Use slicing to print:

```text
The first 4 digits
The last 4 digits
The middle section
```

---

# 7️⃣ STRING METHODS

A **method** is an action attached to a value.

```python
text = "  Hello World  "

print(text.upper())      #   HELLO WORLD
print(text.lower())      #   hello world
print(text.strip())      # Hello World
print(text.title())      #   Hello World
```

## More methods

```python
name = "chris obi"

print(name.title())               # Chris Obi
print(name.replace("obi", "eze")) # chris eze
print(name.count("i"))            # 2
print(name.find("o"))             # 6
print(name.startswith("chris"))   # True
print(name.endswith("obi"))       # True
```

## 🧠 Important

`find()` returns the position, or `-1` if the text isn't found.

---

# 🧠 STRINGS ARE IMMUTABLE

Methods do **not** change the original. They return a **new** string.

```python
name = "  chris  "
name.strip()
print(name)          # still "  chris  "
```

To keep the result, assign it:

```python
name = name.strip()
print(name)          # "chris"
```

You can also chain methods:

```python
name = input("Enter name: ").strip().title()
```

---

# 🧪 PRACTICE 6

Ask for a name. Whatever the user types (`"  aDA oBI  "`), print it cleaned and formatted as `Ada Obi`.

---

# 8️⃣ CHECKING TEXT (BOOLEAN RESULTS)

```python
email = "chris@gmail.com"

print("@" in email)              # True
print("gmail" in email)          # True
print(email.endswith(".com"))    # True
print(email.startswith("chris")) # True
```

These produce `True` or `False`. In Batch 7 you'll use them to make decisions. For now, just print them.

Other useful checks:

```python
"12345".isdigit()    # True
"abc".isalpha()      # True
"abc".isdigit()      # False
```

---

# 🧪 PRACTICE 7

Ask for an email address. Print three checks about it:

```text
Does it contain @?
Does it end with .com?
Is it all lowercase?   (hint: email == email.lower())
```

---

# 9️⃣ f-STRING FORMATTING (REVIEW + STRETCH)

You already know:

```python
print(f"{name} has ₦{balance:,.2f}")
```

Strings can be aligned too:

```python
print(f"{'Item':<10}{'Price':>10}")
print(f"{'Laptop':<10}{250000:>10,}")
```

| Code | Meaning |
|---|---|
| `<10` | left-align in 10 characters |
| `>10` | right-align in 10 characters |
| `^10` | centre in 10 characters |

---

# 🧪 PRACTICE 8

Print a two-column receipt with product names left-aligned and prices right-aligned, using f-string alignment.

---

# 🛠️ DEBUGGING CHALLENGES

Find and fix each bug.

```python
# 1
name = "Chris"
print("Hello " + name + "!)

# 2
age = 25
print("Age: " + age)

# 3
word = "Python"
print(word[6])

# 4
name = "  chris  "
name.strip()
print(f"Hello {name}")   # still has spaces

# 5
print("Chris" - "C")
```

---

# 💰 MINI-PROJECT — WALLET ID GENERATOR

Ask for:

```text
First name
Last name
Phone number (11 digits)
```

Create:

```text
Username  → first letter of first name + last name, all lowercase
Wallet ID → first 3 letters of last name (uppercase) + last 4 digits of phone
```

Example:

```text
Ada, Obi, 08012345678
Username: aobi
Wallet ID: OBI5678
```

---

# 🛒 MINI-PROJECT — RECEIPT HEADER BUILDER

Ask for a store name. Print a centred header:

```text
==============================
        MY STORE NAME
==============================
```

Use `"=" * 30` and `f"{store_name.upper():^30}"`.

---

# 🧠 CHALLENGE — NAME CLEANER

Ask the user to type their full name messily, such as `"   cHRIS    oBI "`.

Output:

```text
Cleaned: Chris    Obi
Length before: 
Length after:
```

Then notice what `.strip()` and `.title()` do and don't fix. (Extra spaces *between* words will remain. That's a good observation to write in your Growth Log.)

---

# 👹 BOSS FIGHT — "THE CUSTOMER PROFILE FORMATTER"

Upgrade your Wallet App and Terminal Store.

Ask for:

```text
Customer full name
Email address
Phone number
Product name
Price
Quantity
```

Your program should:

```text
1. Clean the name (strip + title)
2. Make the email lowercase and stripped
3. Create a username from the email (everything before the @)
4. Mask the phone number: show only the last 4 digits
   Example: *******5678
5. Print a formatted receipt with a centred header
6. Show product name in uppercase
7. Show price, quantity, subtotal with ₦ and commas
```

### Hints

```text
find("@")       → position of @
email[:position] → text before @
"*" * (len(phone) - 4) + phone[-4:]
```

---

# 🚨 BOSS FIGHT RESTRICTIONS

You may use everything from Batches 1–6.

But you are **not yet allowed to use:**

```python
if / elif / else
for / while
def
```

They're still locked. 🔒

---

# 🧪 COMPREHENSION CHECK

Answer without looking back.

### 1.
What is a string?

### 2.
What's the difference between `5` and `"5"`?

### 3.
What does `len("Hello World")` return?

### 4.
Why does indexing start at 0?

### 5.
What does `word[-1]` give you?

### 6.
What is the difference between `word[0]` and `word[0:1]`?

### 7.
Why doesn't this change `name`?

```python
name.upper()
```

### 8.
What does `find()` return when the text isn't found?

### 9.
Why does this fail?

```python
print("Age: " + 25)
```

### 10.
What does `"-" * 10` produce?

---

# 🧠 TRACE THIS PROGRAM

Predict first. Then run it.

```python
text = "  Wallet App  "
clean = text.strip()

print(len(text))
print(len(clean))
print(clean[0])
print(clean[-3:])
print(clean.upper())
print(text)
```

Write down each output and explain why the last line still has spaces.

---

# 🥋 ONE HABIT TO DEVELOP

When working with a string, **draw the boxes** first:

```text
 W  a  l  l  e  t
 0  1  2  3  4  5
```

Then decide which index or slice you need. This habit prevents most off-by-one mistakes.

---

# 💰 CONNECTION TO YOUR WALLET APP

Your wallet can now:

```text
Clean customer names
Build usernames
Create wallet IDs
Mask phone numbers
Format account summaries
```

---

# 🛒 CONNECTION TO YOUR TERMINAL STORE

Your store can now:

```text
Format product names
Build aligned receipts
Print professional headers
Clean customer input
```

Next, in Batch 7, your programs will start **deciding** what to do with this data.

---

# 📈 BATCH 6 EXIT CRITERIA

Before declaring Batch 6 complete, you should be able to:

* [ ] Explain what a string is
* [ ] Use single, double, and triple quotes
* [ ] Use `\n` and `\t`
* [ ] Join strings with `+` and repeat with `*`
* [ ] Use `len()`
* [ ] Use positive and negative indexing
* [ ] Slice strings with `[start:stop]`
* [ ] Use `.upper()`, `.lower()`, `.title()`, `.strip()`, `.replace()`
* [ ] Use `.find()`, `.count()`, `.startswith()`, `.endswith()`
* [ ] Explain why strings are immutable
* [ ] Convert with `str()`, `int()`, `float()`
* [ ] Use `in` to check text
* [ ] Align text in f-strings
* [ ] Build the Wallet ID Generator
* [ ] Complete the Customer Profile Formatter Boss Fight

---

# 📝 GROWTH LOG

```text
## Batch 6 — Growth Log

### 🧠 What clicked?
-

### 🥴 What challenged me?
-

### 🏆 Which exercise am I most proud of?
-

### 🐛 What string bug taught me something?
-

### 👨‍🏫 Could I explain indexing and slicing without looking?
-

### 🔁 What do I need to revise?
-

### 🚀 What can my programs do with text now that they couldn't before?
-
```

---

# 🗺️ PART 1 PROGRESS

```text
PART 1 — PYTHON FOUNDATIONS

[✅] Batch 1 — Programming & Python Basics
[✅] Batch 2 — Core Python Foundations
[✅] Batch 3 — Variables & Assignment
[✅] Batch 4 — Operators & Expressions
[✅] Batch 5 — Input & Output
[✅] Batch 6 — Strings
[🔥] Batch 7 — Conditionals
[🔒] Batch 8 — Loops

            ↓

      🐉 PART 1 BOSS FIGHT
```

---

# 🥋 SENSEI'S FINAL WORD

```text
Batch 3 → "I can store information."
Batch 4 → "I can process information."
Batch 5 → "I can communicate with the user."
Batch 6 → "I can work with text."
```

Next comes a big step:

## 🐍 Batch 7 — Conditionals.
