#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Generate random password list from defined list
# password_letters = random.sample(letters, nr_letters)
# password_symbol = random.sample(symbols, nr_symbols)
# password_numbers = random.sample(numbers, nr_numbers)

# #concatenate strings
# password_list = password_letters + password_symbol + password_numbers
# password_length = nr_letters + nr_symbols + nr_numbers
# #create random list from above generated list
# password_list = random.sample(password_list, password_length)

# #convert list to string
# password_list_str = ""
# for character in password_list:
# 	password_list_str += character

# print(f"Your password is : {password_list_str}")

password_list = []
for char in range(1, nr_letters + 1):
	password_list += random.choice(letters)

for char in range(1, nr_symbols + 1):
	password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
	password_list += random.choice(numbers)

#shuffle the given list 
random.shuffle(password_list)

password = ""

for char in password_list:
	password += char

print(password)




