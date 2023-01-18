number = int(input ('Enter a grade from 0 to 100: '))

if number > 100 or number < 0:
    print ('Number needs to be between 0 through 100')
elif number >= 90:
    print ('Your grade is A')
elif number <=89 and number >= 80:
    print ('Your grade is B')
elif number <=79 and number >= 70:
    print ('Your grade is C')
elif number <=69 and number >= 60:
    print ('Your grade is D')
elif number <=59 and number >= 0:
    print ('Your grade is F')

