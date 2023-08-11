
""" Purpose: To crete a password which suits the requirments described by the user. This includes a unique length along with charcter types used in the password. On top of this the password will have a random order of the desired charceters to allow for maximum security.

    Programer: Nikhil Sinclair 
    
    Date: 07/19/2023
    
"""

import random
import string

def main():
    print("This code is designed to create an ideal password based on your personal preferences.\n")

    length = int(input("How many characters long do you want your password to be?\n"))
    num = int(input("How many of these characters do you want to be numbers?\n"))
    spec = int(input("How many of these characters do you want to be special characters?\n"))
    low_letters = int(input("How many of these characters do you want to be lowercase letters?\n"))
    up_letters = int(input("How many of these characters do you want to be uppercase letters?\n"))

    if length == low_letters + up_letters + num + spec: #checks if passcode requirments satisfy its length
        password = create_password(low_letters, up_letters, num, spec, length) #creates password
        print("Your unique password is:", password) 
        
    else: #if passcode requirments exceed or subceed the length, then password generation is cancelled 
        print("Your chosen characters, numbers, and special characters do not add up to the length of your desired password. Please restart and ensure they do.")


"""
    Puspose: To create a random passowrd based on the users requirments
    
    Parameter 1: low_letter - stores the amount of lower case letters the user wants in their password
    Parameter 2: up_letters - stores the amount of upper case letters the user wants in their password
    Parameter 3: num - stores the amount of integers the user wants in their password
    Parameter 4: spec - stores the amount of special charcaters the user wants in their password
    Parameter 5: length - stores the length of the password
    
    Returns: The created password 
"""

def create_password(low_letters, up_letters, num, spec, length):
    password = ""
    
    #for each type of character for loops are used to generate specific types of charcters multiple times 
    for i in range(low_letters):
        password += random_lowercase()
    for i in range(up_letters):
        password += random_uppercase()
    for i in range(num):
        password += str(random_number())
    for i in range(spec):
        password += random_special()

    password = ''.join(random.sample(password, len(password)))  # Creates unique order for charcater within the password

    return password


"""
Purpose: Generates a random lowercase letters
Returns: Random lowercase letter

"""

def random_lowercase():
    lowercase = string.ascii_lowercase
    return random.choice(lowercase)

"""
Purpose: Generates a random uppercase letters
Returns: Random uppercase letter

"""

def random_uppercase():
    uppercase = string.ascii_uppercase
    return random.choice(uppercase)

"""
Purpose: Generates a random integer from 0-9
Returns: Random integer from 0-9

"""

def random_number():
    return random.randint(0, 9)

"""
Purpose: Generates a random special charcter
Returns: Random special charcter

"""

def random_special():
    special = string.punctuation
    return random.choice(special)

if __name__ == "__main__":
    main()