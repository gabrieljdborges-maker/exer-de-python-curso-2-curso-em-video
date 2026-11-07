maior=0
menor=0
for p in range (1,6):
    x=float(input('Peso da {}ª Pessoa: '.format(p)))
    if p==1:
        menor = x
        maior = x
    else:
        if x>maior:
            maior=x
        if x<menor :
            menor=x
print ('O Maior peso é o de {}Kg\nO Menor peso é o de {}KG'.format(maior,menor))

