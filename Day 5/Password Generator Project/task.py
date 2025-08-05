import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

total_pwd_length: int = nr_letters + nr_symbols + nr_numbers
password: str = ""
pwd_generator: list = ["l", "s", "n"]
for char in range(0, total_pwd_length):
    character = random.choice(pwd_generator)
    if character == "l" and nr_letters > 0:
        password += random.choice(letters)
        nr_letters -= 1
        if nr_letters == 0:
            pwd_generator.remove("l")
    elif character == "s" and nr_symbols > 0:
        password += random.choice(symbols)
        nr_symbols -= 1
        if nr_symbols == 0:
            pwd_generator.remove("s")
    elif character == "n" and nr_numbers > 0:
        password += random.choice(numbers)
        nr_numbers -= 1
        if nr_numbers == 0:
            pwd_generator.remove("n")
print(f"Your password is: {password}")



