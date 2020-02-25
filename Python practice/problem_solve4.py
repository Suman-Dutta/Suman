#LARGEST PALINDROME NUMBER IF 3 DIGIT NO. GIVEN
large=0
for i in range(100,999,1):
    for j in range(100,999,1):
        c=i*j
        if str(c)==str(c)[::-1]:
            #print('Palindrome nos.= ',end=' ')
            #print(c)
            if(large<c):
                large=c
print('Larget Palindrome no.= ',end=' ')
print(large)
                
