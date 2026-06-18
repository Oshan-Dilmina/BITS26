import random
import re

def generatepassword(passwordlength, usenumbers, usecapitalletters, usesimpleletters, usesymbols):
    charpool = ""
    
    if usenumbers == "y":
        charpool  = charpool + '0123456789'
    if usecapitalletters =="y":
        charpool = charpool + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if usesimpleletters == "y":
        charpool = charpool + 'abcdefghijklmnopqrstuvwxyz'
    if usesymbols == "y":
        charpool = charpool + '@#$_'
    
    if len(charpool) == 0:
        print("No characters sets are selected")
    
    while True:
        password = ""

        for i in range(passwordlength):
            password = password + random.choice(charpool)
        
        valid = True

        if usenumbers == "y" and not re.search(r'[0-9]',password):
            valid  = False
        if usecapitalletters == "y" and not re.search(r'[A-Z]',password):
            valid  = False
        if usesimpleletters == "y" and not re.search(r'[a-z]',password):
            valid  = False
        if usesymbols == "y" and not re.search(r'[@#$_]',password):
            valid  = False
        
        if valid:
            return password


passwordlength = int(input("Enter the length of the password. must be longer than or equal 4: "))

usenumbers = input("Use numbers? (y/n):")
usecapitalletters = input("use capitalletters? (y/n):")
usesimpleletters = input("Use simple letters? (y/n):")
usesymbols = input("use @ # $ _  (y/n):")


if passwordlength < 4 or usecapitalletters not in ["y","n"] or usecapitalletters not in ["y","n"] or usecapitalletters not in ["y","n"] or usecapitalletters not in ["y","n"]:
    print("Inavalid inputs or length is less than 4")
else:
    print(generatepassword(passwordlength, usenumbers, usecapitalletters, usesimpleletters, usesymbols))