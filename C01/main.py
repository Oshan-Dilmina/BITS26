import re
import math

password = input("Enter a password: ")

def entropy(password):
        poolsize = 0

        if re.search(r'[a-z]', password):
            poolsize += 26
        if re.search(r'[A-Z]', password):
            poolsize += 26
        if re.search(r'[0-9]', password):
            poolsize += 10
        if re.search(r'[^a-zA-Z0-9]', password):
            poolsize += 5

        entropy = math.log(poolsize,2) *len(password)
        if entropy > 100:
            entropy = 100
        entropy = entropy/10

        if entropy <= 4.9:
            lvl = "Very easy"
        elif entropy <= 7.4:
            lvl = "Easy"
        elif entropy <= 9.4:
            lvl = "Hard"
        else:
            lvl = "Very Hard"

        return round(entropy,1),lvl

#some common passwords like admin and user are not in the list cause they have less than 8 chars
commonpwd = ['password', '123456789', '12345678', '1234567890', 'Password1', 'iloveyou', 'qwerty123', 'sunshine', 'princess', 'admin123', 'P@ssw0rd', 'Admin@123', 'Abcd@1234', 'Pass@123']

if len(password) < 8:
    print("Password is too short! must be at least 8 characters long.")
elif password in commonpwd:
    print("Password is too common! please choose a differrent password.")
elif re.search(r'[^a-zA-Z0-9@#$_.]', password):
    print("Password cant have special characters other that .@#$_ ! please choose a different password.")
elif re.search(r'(.)\1{3,}', password):
    print("Password cant have more than 3 of the same character in a row! please choose a different password.")
elif re.search(r'(..+?)\1', password):
    print("Password can't have repeating sequences! please choose a different password.")
else:
    score,lvl = entropy(password)

    print(f"Password score: {score}")
    print(f"{lvl} to crack")