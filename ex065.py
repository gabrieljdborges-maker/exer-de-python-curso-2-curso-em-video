menor=menor=cont=media=0
soma=0
x=''
while x !='N':
    y = int(input('Digite um numero :'))
    maior=y
    x = str(input('Quer continuar ? [S/N]')).strip().upper()
    cont += 1
    soma += y
    media = soma / cont
    if cont==1:
        menor=maior=y
    else:
        if y>maior:
             maior=y
        elif y<maior :
            menor=y
print('''você digitou {} vezes e a média é {}\nO maior foi o {} e o menor {}'''.format(cont,media,maior,menor))
