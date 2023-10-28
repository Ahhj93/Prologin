K = int(input())  # nombre magique
N = int(input())  # nombre de personnes
tailles = list(map(int, input().split()))  # liste des tailles de chaque personne

inversions = 0

for i in range(N):
    for j in range(i + K, N):
        if tailles[i] > tailles[j]:
            inversions += 1

if inversions % 2 == 0:
    print("OUI")
else:
    print("NON")
