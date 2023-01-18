StringS = input('Enter a string: ')

#the size amount of the user input - string
size = len(StringS)

#Storage for lower case string and upper case string
lc = ""
uc = ""

for i in range(0, size, 1):
    
    
    letter = StringS[i]

    if (letter >= 'A' and letter < 'Z'):
        uc += letter

    else:
        lc += letter

print(lc + uc)