from random import randint

k = randint(1, 1000)
n = randint(1, 1000)
print(k)
print(n)
for i in range(n):
    print(randint(1, 1000), end=" " if i < n - 1 else "\n")