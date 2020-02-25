#difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
sum1=0
sum2=0
for i in range(1,101,1):
    sum1=sum1+i*i
    sum2=sum2+i
sum3=sum2*sum2
d=(sum2**2)-sum1
print('Sum of squares of nos.= ',end=' ')
print(sum1)
print('Sum of square of sum= ',end=' ')
print(sum3)
print('difference ',end=' ')
print(d)
