# import random
import random
# variables -> guess & num
guess = None
num = random.randint(1,10)
# while loop
while guess != num:
    try:
        guess = int(input('Enter anumber from 1-10: '))

        if guess == num:
            print('Congs for guessing the number correctly')
            break
        else:
            print('Nope, kindly try again!')
    except ValueError:
        print('Oooops, that aint a number! Try Again')
