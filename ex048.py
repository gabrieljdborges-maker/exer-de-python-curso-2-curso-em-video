print('-=-='*25)
print('nesse programa iremos mostrar a soma de multiplos de 3 entre 1 e 500')
print('-=-='*25)
i=int(input('Informe o valor do inicio '))
f=(int(input('Informe o valor do fim ')))
y=0
for x in range (i,f):
  if x % 3 == 0 and x % 2!= 0 :
      y += x
print (y)
