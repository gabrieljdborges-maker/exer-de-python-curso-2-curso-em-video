soma=cont=0
while True:
    x=int(input('Informe o valor : digite 999 para Parar '))
    if x == 999:
        break
    cont += 1
    soma += x
print(f'Você informou {cont} numeros e a soma dele é {soma}')