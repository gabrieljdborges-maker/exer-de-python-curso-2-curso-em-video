import random
from time import sleep as s


print('=-=-'*20)
print('nesse programa iremos jogar JO KEN PO Contra o PC ')
print ('=-=-')

print('''Essas são suas opções 
[ 0 ] Pedra
[ 1 ] Papel 
[ 2 ] Tesoura''')
x=int(input('Qual sua opção ? '))
y=random.randrange(3)
s(1)
print ('JO')
s(1)
print('KEN')
s(2)
print('POO')
s(2)
if x==0 and y==1 :
    print ('''Você perdeu, tente novamente :(
Você escolheu Pedra e o PC escolheu Papel ''')

elif x==0 and y==2:
    print ('''Você vendeu !!! 
Você escolheu Pedra e o PC escolheu Tesoura ''')

elif x==1 and y==0:
    print(''' Você venceu !!!
Você escolheu Papel e o PC escolehu Pedra''')

elif x==1 and y==2 :
    print ('''Você perdeu, tente novamente :(
Você escolheu o Papel e o PC escolhei a Tesoura''')

elif x==2 and y==0:
    print ('''Você perdeu, tente novamente :(
Você escolheu tesoura e o Pc escolheu Pedra''')

elif x==2 and y==1:
    print (''' Você Venceu !!!
Você escolheu a Tesoura e o PC escolheu o Papel''')

elif x==y:
    print ('Empatou jogue novamente')

else:
    print('você informou um numero incorreto, tente novamente. ')