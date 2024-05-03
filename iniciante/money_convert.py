def convert_origem_to_strange():
    moeda_origem = str(input('Digite o nome da moeda que possuí: '))
    moeda_estrangeira = str(input('Digite o nome da moeda para a qual quer converter: '))
    valor_estrangeiro = float(input(f'Digite o valor de mercado da moeda {moeda_origem} em relação a moeda {moeda_estrangeira}: '))
    valor_origem = float(input('Digite quanto quer converter: '))
    
    if valor_estrangeiro < 1:
        conversao = valor_origem * (valor_estrangeiro * 10)
        print(f'{conversao:.2f} {moeda_estrangeira}')
    else:
        conversao = valor_origem / (valor_estrangeiro)
        print(f'{conversao:.2f} {moeda_estrangeira}')

convert_origem_to_strange()

