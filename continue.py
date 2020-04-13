spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('Spam is ' + str(spam))


#Spam is 3 is not printed because the condition is met for the continue statment to skip print and go back to the start of the loop