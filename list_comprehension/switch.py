def get_tipo_dia(dia):
    dias = {
        (1,7): 'Fim de semana',
        tuple(range(2,7)): 'Dia de semana',
    }
    dia_escolhido = (tipo for numeros, tipo in dias.items() if dia in numeros)
    return next(dia_escolhido, "** Valor Invalido **")

if __name__ == '__main__':
    for i in range(0 , 9):
        print(f'{get_tipo_dia(i)}')