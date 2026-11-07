from time import sleep
print(' Olá estamos iniciando mais um exercicio , aguarde alguns segundos')
sleep(3)
n1=int(input('Digite o primeiro numero Inteiro : '))
sleep(3)
n2=int(input('Digite o segundo numero Inteiro : '))
sleep(3)
if n1>n2:
    print ('O numero {} é maior que o numero {}'.format(n1,n2))
elif n2>n1:
    print ('O numero {} é maior que o numero {}'.format(n2,n1))
else:
    print ('Os dois numeros são o {}, com isso são iguais !!!'.format(n1))
