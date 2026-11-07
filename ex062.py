from functools import total_ordering
from time import sleep
p=int(input('Informe o valor do primeiro termo :'))
r=int(input('Informe o valor da razão: '))
t=p
c=1
mais=10
total=0
while mais!=0:
    total=total+mais
    while c<=total:
        print('{}==>'.format(t), end='')
        t+=r
        c += 1
    print ('Pausa')
    mais=int(input('Informe mais quantos termos quer ver: '))
print('Para essa PA foram mostrados {} termos '.format(c))
