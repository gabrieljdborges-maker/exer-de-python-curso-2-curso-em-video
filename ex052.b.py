tot=0
c=int(input('Digite um numero : '))
for num in range (1,c+1):
    if c % num == 0 :
        print('\033[32m', end=' ')
        tot+=1
    else:
        print('\033[34m', end=' ')
    print('{}'.format(num),end=' ')
if tot==2:
    print('\n{} é primo por ser divisivel {} vezes'.format(c,tot))
else:
    print('\n{} não é primo por ser divivivel {} vezes.'.format(c,tot))
