n=input('Enter a text number:')
list=n.split()
sum=0
for i in list:
    sum=sum+int(i)
print('The sum of the numbers is:',sum)