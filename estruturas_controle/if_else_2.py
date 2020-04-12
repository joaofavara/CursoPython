def faixaEtaria(idade):
   if 0 <= idade < 18:
      return 'Menor de idade'
   elif idade in range(18, 65):
      return 'Adulto'
   elif idade in range(66, 100):
      return 'Melhor idade'
   elif idade >= 100:
      return 'Centenario'
   else:
      return 'Idade invalida'

if __name__ == '__main__':
      for idade in (12, 23, 43, 35, 0, 102, -3):
         print(f'{idade} -> {faixaEtaria(idade)}')