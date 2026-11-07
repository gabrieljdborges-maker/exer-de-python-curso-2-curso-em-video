from time import sleep as s

print('Neste programa iremos mostrar se o numero é binario, octal ou hexadecimal')
#s(3)
num=int(input("Digite o numero : "))
print('''Escolha a uma base para conversão 
 [1] converter para Binario 
 [2] Converter para Octal 
 [3] Converter para Hexadecimal ''')
op=int(input('Qual é sua opção ? '))
if op==1:
    print('Convertendo o {} para Binario é igual a {}'.format(num, bin(num)[2:]))
elif op==2:
    print('Convertendo o {} para Octal é igual a {}'.format (num,oct(num)[2:]))
elif op==3:
    print('convertendo o {} para Hexadecimal é igual a {}'.format(num,hex(num)[2:]))
else:
    print ('Opção invalida tente novamente  o numero errado ')
