import csv

with open('desafio-ibge.csv', encoding='latin1') as ibge:
    dados = csv.reader(ibge)
    for cidade in dados:
        print(f'{cidade[8]}: {cidade[3]}')