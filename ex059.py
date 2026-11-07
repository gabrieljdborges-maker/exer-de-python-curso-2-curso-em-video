print('\033[35m-=-='*20)
print('\033[33m Menu para calculos Simples')
print('\033[35m-=-='*20)
menu=0
x=int(input('\033[33mInforme o primeiro valor: '))
y=int(input('\033[033mInforme o segundo valor: '))
while menu!=5:
    menu=(int(input('''\033[033m\nescolha a opção que deseja\n[1] - SOMA\n[2] - MULTIPICAÇÃO\n[3] - MAIOR\n[4] - NOVOS NUMEROS \n[5] - SAIR DO PROGRAMA ''')))
    maior=x
    if menu == 1:
        print('\033[31mA soma é igual a {}'.format(x+y))
    elif menu == 2:
        print('\033[31mA multiplicação é igual a {}'.format(x*y))
    elif menu == 3:
        if x>y:
           print('\033[31mO {} é maior que o {}'.format(x,y))
        else:
            print('\033[31mO {} é maior que o {}'.format(y,x))
    elif menu == 4:
        x = int(input('\033[34mInforme o novo primeiro valor: '))
        y = int(input('\033[034mInforme o novo segundo valor: '))
    else:
        print('\033[32mObrigado, até a proxima.\n \033[31mPROGRAMA FECHADO ')