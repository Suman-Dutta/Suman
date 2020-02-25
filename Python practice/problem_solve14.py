#The following iterative sequence is defined for the set of positive integers:

#n → n/2 (n is even)
#n → 3n + 1 (n is odd)

#Using the rule above and starting with 13, we generate the following sequence:

#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

#Which starting number, under one million, produces the longest chain?
num=[]
longseq=0
count=0
i=2
num1=1000000
for i in range(2,1000000,1):
    while(num1>1):
        if num1==1:
            break
        elif num1%2==0:
            num1=num1/2
            num.append(num1)
            count=count+1
        else:
            num1=num1*3+1
            num.append(num1)
            count=count+1
        
    
    if(longseq<count):
        longseq=count
    else:
        print(longseq)
        for i in range(1,1000000,1):
            print('Enter longest chain= ',end='')
            print(num[i])
            break
    num1-=1
