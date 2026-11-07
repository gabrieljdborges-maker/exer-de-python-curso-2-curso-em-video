from time import sleep as s

print('------'*20)
print('Nesse programa iremos fazer um simulador de sistema de Loja Borges : ')
print('------'*20)
s(3)

valor=float(input('Qual o valor total da compra : R$ '))
print('''Opções de pagamento : 
[ 1 ] A vista dinheiro ou cheque :
[ 2 ] A vista no cartão :
[ 3 ] parcelado 2 x :
[ 4 ] parcelado 3 x ou mais :''')

pagamento=int(input('Qual é a opção de pagamento ? '))
dinheiro=valor-(valor*0.1)
vistac=valor-(valor*0.05)
parcelado=valor+(valor*0.2)
s(3)
if pagamento==1:
   print('O valor a ser pago é de {}'.format(dinheiro))
elif pagamento==2:
   print('O valor a ser pago é de {}'.format(vistac))
elif pagamento==3:
    print('O valor a ser pago é de {} e será pago em duas parcelas de {}'.format(valor,valor/2))
elif pagamento == 4:
    parcelas=int(input('Informe o numero de parcelas '))
    print('O valor a ser pago é de {} e será pago em {}, cada uma no valor de {}'.format(parcelado,parcelas,parcelado/parcelas))
else :
    print('A forma de pagamento foi inserida incorretamente.')

