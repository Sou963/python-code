from random import randint
for i in range(6):
    guessnumber=int(input('Enter a number 1 to 10:'))
    number=randint(1,10)
    if guessnumber==number:
     print('Congratulations! You guessed the number.')
    else:
     print('Sorry, the number was', number) 
    