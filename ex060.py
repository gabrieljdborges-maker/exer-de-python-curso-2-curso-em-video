from math import factorial
fat=1
i=1
menu=1
x = int(input('Informe o valor de um numero: '))
while menu !=0:
    menu=int(input('\033[32m''\n[1]FATORIAL\n[2] novos numeros\n[0]Para sair do programa'))
    if menu == 1:
       print('\033[34m''O valor do Fatorial de {} é {}'.format(x,factorial(x)))
    elif menu == 2:
        x = int(input('\033[34m''Informe o novo valor de um numero: '))
    else:
       print('\033[31m''Estamos fechando o programa, até a proxima.')
