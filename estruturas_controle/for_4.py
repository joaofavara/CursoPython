from random import randint

def sortear_dado():
    return randint(1, 6)

dado = sortear_dado()

for i in range(1, 7):
    if i % 2 == 0:
        if i == dado:
            print(f'Acertou ... {dado}')
            break
    else:
        continue
else:
    print('Nao acertou o numero ...')