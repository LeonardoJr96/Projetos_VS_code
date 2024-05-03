lista = []

def logica(quantidade):
    
    for i in range(quantidade):
        num = int(input("digite o numero da lista: "))
        lista.append(num)

def ordenar():
    
    quantidade = int(input('quantos numeros serão para ordenar: '))
    ordem = str(input('ordenar crescente (1) ou decrescente (2): '))

    if ordem == '1' or ordem == 'crescente':
        logica(quantidade)
        lista.sort()
        print(lista)
    else:
        logica(quantidade)
        lista.reverse()
        print(lista)

ordenar()