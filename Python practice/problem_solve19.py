#You are given the following information, but you may prefer to do some research for yourself.

#1 Jan 1900 was a Monday.
#Thirty days has September,
#April, June and November.
#All the rest have thirty-one,
#Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

print('Enter the year= ',end=' ')
year=input()
jan=31
mar=31
apr=30
may=31
june=30
july=31
aug=31
sept=30
oct=31
nov=30
dec=31
#need to check whether leap year or not
for i in range(int(year),2001,1):
    if (i%4==0):
        if (i%100==0):
            if (i%400==0):
                print('Its a Leap Year')
                feb=29
            else:
                print('Not a leap year')
                feb=28
        else:
            print('Its a Leap Year')
            feb=29
    else:
        print('Not a leap year')
        feb=28
