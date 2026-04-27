#1^1+2^2+3^3+___+n^n
n=int(input('Enter a number:'))
sum=0
for i in range(1,n+1,1):
    sum=sum+i**1
print('print the sum',sum)