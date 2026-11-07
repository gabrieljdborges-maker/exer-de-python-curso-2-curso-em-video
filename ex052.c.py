num=int(input('Digite um numero: '))
soma=0
for x in range(1,num+1):
    if num % x == 0:
        print ('\033[032m', end=' ')
        soma+=1
    else:
        print('\033[031m' ,end=' ')
    print('{}'.format(x), end='')
if soma == 2:
    print('\033[035m''\nO {} é divisivel por {} numeros por isso é primo'.format(num,soma))
else :
    print('\033[034m''\nO {} é divisivel por {} numeros, por isso não é primo'. format(num,soma))
