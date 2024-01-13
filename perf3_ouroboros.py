from random import randint, choice

n = randint(2, 100_000)
m = randint(1, 2_000_000)
actions_choix = ['C', 'A', 'R', 'M']
villes_restantes = n
actions = []
for i in range(m):
    if villes_restantes <= 1:
        actions.append(choice(actions_choix[:-1]))
    elif villes_restantes == n:
        actions.append(choice(actions_choix[1:]))
    else:
        actions.append(choice(actions_choix))
    if actions[-1] == 'C':
        villes_restantes += 1
    elif actions[-1] == 'M':
        villes_restantes -= 1
print(n)
print(m)
for i in range(n):
    print("{0}heim".format(i))
for a in actions:
    print(a, end="")
print()