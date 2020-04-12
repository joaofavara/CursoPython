from random import randint

valor_input = -1
valor_randomico = randint(0, 9)

while valor_input != valor_randomico:
    valor_input = int(input('Chute um valor: '))

print('O numero secreto era {}'.format(valor_randomico))