import string
import random

def password_gen(keys):
    final_password = ""
    for n in range(keys):
        possibilities = random.randint(0,94)
        final_password += string.printable[possibilities]     # within the printable list of 94 items, select one.
    return final_password

print password_gen(10)