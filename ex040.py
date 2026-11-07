from time import sleep
print('-=-='*20)
print('Este programa mostra sua média no ano, Aguarde alguns segundos....')
print('-=-='*20)
sleep(3)
nome=str(input('Poderia Informar sue nome')).strip().title()
sleep(3)
n1=float(input('Informe o valor da  n1 : '))
n2=float(input('informe o valor da n2 : '))
sleep(3)
nota=(n1+n2)/2
if nota<5:
    print ('{}, você está reprovado e sua média é {:.1f} '.format(nome,nota))
elif nota>=5 and nota<=6.9:
    print (' {} você está de recuperação , sua média é {:.1f} '.format(nome,nota))
else:
    print ('Parabens {} !!!!!!\n Você foi aprovado com uma média de {}'.format(nome,nota))
