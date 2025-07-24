import random
import string
import sys
from random import choice
import pyperclip

my_password = []
print("----- Random Password Generator ------")
pswd_length = int(input("Enter Password Length : "))

if pswd_length < 8 or pswd_length > 20:
    print("Password Minimum Length is 8 and Maximum Length is 20")
    sys.exit()
else:
    Password_List = string.ascii_letters + string.digits + string.punctuation
    for a in range(pswd_length):
        my_password.append(random.choice(Password_List))

    string_pswd = "".join(my_password)
    print(f"Generated Password : {string_pswd}")

    choice = input(f"Do you want to copy {string_pswd} ?")
    if choice.lower() == "yes":
        pyperclip.copy(string_pswd)
        print("Password Has been Copied")