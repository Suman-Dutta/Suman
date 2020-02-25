#Sum of all primes in 2 million
sum=0

for i in range(2,10,1):
    for j in range(i,10,1):
        if(i%j==0):
            break
        else:
            #print('the prime numbers are= ',end='')
            #print(i)
            sum=sum+i

print('the sum of prime numbers= ',end=' ')
print(sum)
#not done
