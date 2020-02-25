#What is the value of the first triangle number to have over five hundred divisors?

counter = 0
n = 1

while counter <500:
    counter = 2
    n += 1

    triangle = n*(n+1)/2
    for i in range(2, int(triangle**0.5)):
        if triangle % i == 0:
            counter += 2

    print(triangle)
