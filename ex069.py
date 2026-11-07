c=mulher=homem=0
print('~~'*20)
print ('PESQUISA')
print('~~'*20)
while True :
    idade = int(input('Idade : '))
    if idade >=18 :
        c+=1
    sexo=' '
    while sexo not in 'FM':
        sexo=str(input('Sexo : [F/M ')).strip().upper()[0]
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        print()
        print('~~' * 20)
        print('CADASTRANDO NO BANCO DE DADOS')
        print('~~' * 20)

    if sexo == 'F':
        if idade<20:
            mulher+=1

    if sexo == 'M':
        homem+=1

    if continuar =='N':
        print('~~' * 20)
        print('Encerrando a pesquisa')
        print('~~' * 20)
        print (f'Nessa pesquisa tivemos {c} maiores de idade\nTivemos um total de {homem} homens\nTivemos {mulher} mulheres com idade menor de 20 anos  ')
        break

