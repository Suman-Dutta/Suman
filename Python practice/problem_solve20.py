#Find the sum of the digits in the number 100!
print('Enter the factorial of no.= ',end=' ')
num=input()
mul=1
s=0
for i in range(1,int(num)+1,1):
    mul*=i
print('Factorial result= ',end=' ')
print(mul)
while(mul>0):
    s+=mul%10
    mul=(mul//10)
print('sum of factorial digits= ',end=' ')
print(s)
