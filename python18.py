text=input('Enter a text number:')
numLetter=0
numDigit=0
numWords=0
for i in text:
    if i.isalpha():
        numLetter+=1
    elif i.isdigit():
        numDigit+=1
    elif i.isspace():
        numWords+=1
print('Number of letters:',numLetter)
print('Number of digits:',numDigit)
print('Number of words:',numWords)