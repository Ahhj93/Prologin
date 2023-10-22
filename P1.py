N = int(input())
differences = list(map(int, input().split()))
hauteur = [1]
for i in range(N):
    hauteur.append(hauteur[i] + differences[i])
saut = [hauteur[i] - hauteur[i-1] for i in range(1, N+1)]
max_hauteur = max(hauteur)
indice_max = hauteur.index(max_hauteur)
if indice_max == 0:
    max_saut = 0
else:
    max_saut = max(saut[:indice_max])
print(max_saut)