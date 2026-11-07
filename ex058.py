from random import randint
from time import sleep as s
x=randint(0,10)
y=''
soma=1
print('\033[33m','-=-='*20)
print('\033[34m''JOGO DE ADIVINHAÇÃO ')
print('\033[33m','-=-='*20)
while y != x:
    y=int(input('\033[34mTente adivinhar o numero :'))
    print('\033[35m VERIFICANDO....')
    s(2)
    if y!=x:
        soma+=1
        print('\033[31m','Numero errado tente novamente')
    if y==x :
        print ('\033[32m','PARABENS VOCÊ ACERTOU O NUMERO É : {} !!!!\n VOCÊ ACERTOU EM {} TENTATIVAS '.format(x,soma))


