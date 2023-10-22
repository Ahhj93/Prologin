import random

n = random.randint(1, 20)

print(f"{n}")
for i in range(0,n):
	r = random.randint(-1000, 1000)
	print(f"{r}", end='')
	if(i != n-1):
		print(" ", end='')
print("")