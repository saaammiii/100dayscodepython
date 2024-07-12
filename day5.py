# password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!!")
no_of_letters = int(input("How many letters would you like in your password?\n"))
no_of_symbols = int(input("How many symbols would you like?\n"))
no_of_digits = int(input("How many numbers would you like?\n"))

password_list = []
for char in range(1,no_of_letters+1):
    password_list.append(random.choice(letters))

for sym in range(1,no_of_symbols+1):
    password_list.append(random.choice(symbols))

for dig in range(1,no_of_digits+1):
    password_list.append(random.choice(numbers))


# print(password_list)
# print(random.shuffle(password_list))
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"Here is your password:  {password}")