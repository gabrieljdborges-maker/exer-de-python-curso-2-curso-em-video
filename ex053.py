
frase=str(input('Poderia informar a frase : ')).strip().lower().replace('','')
f2=frase[::-1]
if f2 == frase:
    print ('é um polimdromo, pois {} e {} são iguais '.format(frase,f2))
elif f2 != frase:
    print('Não é um polimdromo pois {} não é igual a {}'.format(frase,f2))