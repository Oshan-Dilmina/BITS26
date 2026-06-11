string = input("Enter a string: ")
stringsplit = string.split()

reverse = []


for i in range(len(stringsplit)):
    for x in range(len(stringsplit[i])):
        reverse.append(stringsplit[i][len(stringsplit[i])-x-1])
    reverse.append(" ")    
    

reverse = "".join(reverse).strip()

print(reverse)

if reverse == string:
    print("Palindrome")
