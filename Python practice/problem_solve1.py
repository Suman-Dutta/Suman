#sum of multiples of 3 or 5 below 1000
count=0
sum=0
for i in range(0,1000,1):
    if((i%3==0) or (i%5==0)):
     count=count+1
     sum=sum+i**i
print('The nos. count= ')
print(count)
print('\0')
print('the sum of multiples= ')
print(sum)
