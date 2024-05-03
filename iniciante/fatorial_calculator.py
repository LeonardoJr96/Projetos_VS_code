def fatorial():
    
    fat = 1
    num = int(input('Fale o o número para cálcular o fatorial: '))
    for number in range(num):
        fat = fat + (fat * number)

    print(fat)

fatorial()

