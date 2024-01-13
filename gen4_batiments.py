from random import randint

n = randint(1, 1000)
r = randint(1, 1000)
k = randint(1, 1000)
print(n)
print(r)
print(k)
for i in range(n):
    print(randint(1, 1000), end=" " if i < n - 1 else "\n")