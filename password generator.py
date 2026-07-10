import random
import string
import pyperclip


def get_positive_int(prompt):
    while True:
        try:
            val = int(input(prompt))
            if val >= 0:
                return val
            print("Enter positive number.")
        except ValueError:
            print("Enter valid number.")

print("Welcome to PyPassword Generator!\n")

nr_letters = get_positive_int("How many letters?\n")
nr_numbers = get_positive_int("How many numbers?\n")
nr_symbols = get_positive_int("How many symbols?\n")

all_chars = (
    random.choices(string.ascii_letters, k=nr_letters) +
    random.choices(string.digits, k=nr_numbers) +
    random.choices('!#$%&()*+-_[]{}:;"\'|/?^`~=', k=nr_symbols)
)

random.shuffle(all_chars)
password = ''.join(all_chars)

print(f"\nYour password is: {password}")
pyperclip.copy(password)
print("copied in clipboard!")
