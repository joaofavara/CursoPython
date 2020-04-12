palavra = 'paralelepipedo'

for letra in palavra:
    print(letra, end=',')

nomes = ['Joao', 'Pedro', 'Miguel', 'Angelo', 'Helena']

for nome in nomes:
    print(nome)

for index, nome in enumerate(nomes):
    print(f'{index + 1}) {nome}')

dia_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta'
                'Quinta', 'Sexta', 'Sabado')

for dia in dia_semana:
    print(f'Hoje eh dia {dia}')

for numero in {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}:
    print(numero)