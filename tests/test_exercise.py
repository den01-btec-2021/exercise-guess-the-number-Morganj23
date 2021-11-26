


import random
n = random.randint(0,9)


guess = int(input('pick a number between 1 and 10: '))

while n != 'guess':
    print
    if guess < n:
        print ('guess is low')
        guess = int(input('Enter a number between 1 and 10: '))
    elif guess > n:
        print ('guess is high')
        guess = int(input('Enter a number betwen 1 and 10: '))
    else:
        print ('you did it')
        break
    assert 0==0
