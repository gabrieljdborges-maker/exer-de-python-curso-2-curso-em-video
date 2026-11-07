from datetime import date
from time import sleep
#decorando algumas funções para deixar o programa completo

print('°X°'*20) # deixando o programa mais bonito
print ('Este programa será usado para definir sua categoria !!\n Aguarde alguns segundos.....')
print('°X°'*20)
sleep(3)
nome=str(input('Informe seu nome : ')).strip().title()
ano=int(input('Informe o ano do seu nascimento : '))
sleep(3)
anoatual= date.today().year
idade=abs(ano-anoatual)
if idade<=9:
    print('{} sua categoria é Mirim, pois sua idade é {} anos '.format(nome,idade))
elif idade <=14:
    print ('{} sua categoria é Infantil, pois sua idade é  {} anos '. format(nome,idade))
elif idade <=19:
    print('{} sua categoria é Junior, pois sua idade é {} anos'.format (nome,idade))
elif idade <= 25:
    print ('{} sua categoria é a Senior, pois sua idade é {} anos.'.format(nome,idade))
else :
    print ('{} sua categoria é a Master, pois sua idade é  {} anos'.format(nome,idade))
