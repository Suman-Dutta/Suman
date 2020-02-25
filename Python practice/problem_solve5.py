#smallest number that is divisible by a no. from 1 to 20 ex-2520 divisble by all no. 1-10

#import array
#arr=array.array('k')
#z=1
#count=0
#for i in range(9999,1,-1):
#    for j in range(1,10,1):
#        if(i%j==0):
#            count=count+1
#            if(count==10):
#                for k in range(z,100,1):
#                    arr[k]=i
#                z=z+1
#        else:
#            break
#for l in range(1,100,1):
#    print(arr[l])
#for m in range(1,100,1):
#    if(arr[l]<arr[l+1]):
#        small=arr[l]

#print('Smallest no.= ',end=' ')
#print(small)
def smallest_multiple(upper_limit):
    test_num = upper_limit
    while True:
        count = 0
        for i in range(1, upper_limit + 1):
            if test_num % i == 0:
                count = count + 1
        if count == upper_limit:
            return test_num
        else:
            test_num = test_num + i
            #print(test_num)

r = smallest_multiple(int(input("Enter upper bound : ")))
print("Answer is {}".format(r))
