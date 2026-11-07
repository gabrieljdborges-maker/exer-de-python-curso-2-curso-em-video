tot=0

num=int(input('Informe um valor'))
for c in range (1,num+1):
    if num % c  == 0:
        print('\033[33m', end= ' ')
        tot += 1
    else :
         print('\033[31m', end=' ')
    print('{}'.format(c), end='')
print('\n\033[32m {} numero foi divisivel {}'.format(num,tot))
if tot ==2 :
    print('o {} é primo'.format(num))
else :
    print ('O {} não é primo, ele é divisifel por {} numeros'.format(num,tot))
