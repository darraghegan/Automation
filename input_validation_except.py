print('How many cats do you own?')
numcats = input()

try:
    if int(numcats) <= 0:
        print("You don't have any cats")
    elif int(numcats) >= 4:
        print("That's a lot of cats")
    else:
        print('That is not that many Cats.')
except ValueError:
    print('You did not enter a number')