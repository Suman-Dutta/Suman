#pythagorean triplet
product=0
for i in range(1,1000,1):
    for j in range(i+1,1000,1):
        num3=1000-i-j
        if (num3*num3==i*i+j*j):
                product=(i*j*num3)
                break
print('The product of Pythagorean triplet= ',end=' ')
print(product)
