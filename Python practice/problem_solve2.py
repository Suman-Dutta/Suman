#sum of even valued nos. in fibonacci sequence not exceeding 4 million
dig1=1
dig2=2
dig3=0
sum=0
print('how many terms= ')
c=input()
print('The fibonacci sequence= ')
print(dig1,end=' ')
print(dig2,end=' ')
for i in range(1,int(c),1):
    dig3=dig1+dig2
    print(dig3,end=' ')
    if((dig3%2==0) and (dig3<4000000)):
        sum=sum+dig3
    dig1=dig2
    dig2=dig3

print('\0')
print('the sum of even valued sequence= ',end=' ')
print(sum+2)
