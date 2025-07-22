import random as rd
import sys
import string

pakistan_cities = [
    "Karachi",
    "Lahore",
    "Islamabad",
    "Rawalpindi",
    "Faisalabad",
    "Multan",
    "Peshawar",
    "Quetta",
    "Sialkot",
    "Gujranwala"
]
print(pakistan_cities)
print(rd.sample(pakistan_cities,3))
rd.shuffle(pakistan_cities)
print(pakistan_cities)
print(rd.choice(pakistan_cities))

print("******** Random Number Guessing Game *******\n")
Computer_number = rd.randint(1, 20)
lives = 3

while lives > 0 :
    user_input = int(input("Enter Any Number between 1 - 20: "))


    if user_input == Computer_number:
        print("Congratulations You've Guessed!!")
        sys.exit()

    else:
        lives -= 1

    if user_input > Computer_number:
        print("* Hint: Think Lower Number")
    elif user_input < Computer_number:
        print("*Hint: Think Higher Number")

    if lives == 0:
        print("Lives Ended")
    else:
        print(f"{lives} Remaining")


print(string.digits)
print(string.ascii_letters)
print(string.punctuation)
print(string.whitespace)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.hexdigits)
