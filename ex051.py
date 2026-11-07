
print('=-=-'*25)
print('Programa para mostrar os 10 primeiros termos de uma PA')
print('-=-='*25)

p1=int(input('Informe o valor do primeiro termo'))
r=int(input('Informe o valor da razão'))
decimo=p1+ (10-1)* r
for x in range (p1,decimo,r):
    print(x)