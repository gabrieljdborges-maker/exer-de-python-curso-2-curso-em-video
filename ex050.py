cont=0
soma=0
print('=-=-'*25)
print('Programa para somar 6 numeros pares')
print('-=-='*25)
for x in range (1,7):
  num=(int(input('Informe o {} valor'.format(x))))
  if num % 2 == 0:
    soma= soma + num
    cont = cont + 1
print ('Você informou {} numeros Pares e a soma é de {}'. format (cont, soma))
