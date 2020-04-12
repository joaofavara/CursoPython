import sys
import errno


def conceitosNotas(valor):
    nota = float(valor)
    if nota >= 9.1:
       return 'A'
    elif nota >= 8.1:
       return 'A-'
    elif nota >= 7.1:
       return 'B'
    elif nota >= 6.1:
       return 'B-'
    elif nota >= 5.1:
       return 'C'
    elif nota >= 4.1:
       return 'C-'
    elif nota >= 3.1:
       return 'D'
    elif nota >= 3.1:
       return 'D-'
    elif nota >= 1.1:
       return 'E'
    else:
       return 'E-'


if __name__ == '__main__':
    if float(sys.argv[1]) > 10 or float(sys.argv[1]) < 0:
        print('Erro: paramentro invalido')
        sys.exit(errno.EPERM)
    else:
        conceito = conceitosNotas(sys.argv[1])
        print('Nota {} => {}'.format(sys.argv[1], conceito))
