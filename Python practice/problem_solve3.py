#largest prime factor 600851475143

n = int(input('The largest prime factor of= '))

p = 2
while (p*p <= n):
  if (n % p == 0):
    n //= p
  else:
    p += 2 if p>2 else 1   # after 2, consider only odd p

print("is", n)
