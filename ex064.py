y=x=cont=0
while y!=999:
    y=int(input('informe um valor inteiro \n[digite 999 para finalizar o programa]'))
    if y!=999:
        x+=y
        cont+=1
    else:
        print('Você digitou {} numeros e a soma deles é {}'.format(cont,x))
print('Fim')
