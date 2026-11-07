fat=1
i=1
x=int(input('Informe o valor '))
for i in range(1,x+1):
    fat*=i
print('O fatorial do numero {}! é igual a {}'.format(x,fat))
