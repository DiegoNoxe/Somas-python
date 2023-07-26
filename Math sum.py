print('Soma no pycharm')
print()
def hope():
    try:
     n1 = int(input('Primeiro número: '))
     n2 = int(input('Segundo Número:'))
     s  = n1 + n2
     print()
     print('A soma de {} + {} é igual: {}'.format(n1,n2,s))
    except ValueError:
        print()
        print('Opção invalida! Tente novamente!')
        print()
        hope()
hope()