produto = {
    'nome': 'PS5',
    'preco': 200.00,
    'impotado': True,
    'estoque': 3
}

for chave in produto:
    print(chave)

for value in produto.values():
    print(value)

for chave, value in produto.items():
    print(f'{chave} -> {value}')