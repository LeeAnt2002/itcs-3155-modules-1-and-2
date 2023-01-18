baseinput = int( input('Enter an interger greater than 1: ') )
if baseinput <= 1:
    print('Sorry the number has to be greater than 1, Try Again please')
else:
    for i in range (baseinput + 1):
        print("The cube of " + str(i) + " is " + str(pow(i,3)) )