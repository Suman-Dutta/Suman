#How many such routes are there through a 20×20 grid?
#by combinametrics I saw that out of 2n ways we take inly n ways
p=1
path=1
print('Enter grid size= ',end=' ')
grid=input()
for i in range(0,int(grid),1):
    path*=(2*int(grid))-i
    p*=i+1
move=path/p
print('Total moves= ',end=' ')
print(move)
