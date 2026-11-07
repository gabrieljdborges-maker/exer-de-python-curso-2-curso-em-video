n=int(input('Qual o numero que você quer o Fatorial ?'))
c=n
fat=1
while c>0:
    print (c, end='')
    print(' x ' if c>1 else ' = ', end='')
    fat*=c
    c -= 1
print(fat)