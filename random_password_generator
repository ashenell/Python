"""
Author: Rauno Vaher
Github: Ashnell
Random password generator
"""
#Libaries

import random, string

#Creating a variable that asks for user password leng integer not in string.

lenght = int(input("How long passwor do you need? "))
#variable imports strings, idivifal characters
password_char = string.ascii_letters + string.digits + string.punctuation
#Creat a list in to brackets
password = []
# in the x we say number of times based on the length password should be
for x in range(lenght):
    password.append(random.choice(password_char))
print(''.join(password))
