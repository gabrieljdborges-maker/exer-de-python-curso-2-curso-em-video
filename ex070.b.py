soma=cont=0
while True :
    preço=int(input('Informe o preço do Produto : '))
    nome=str(input('Informe o nome do Produto : '))
    soma+=preço
    menor=preço
    mp=nome
    x=str(input('Quer cadastrar mais algum item ?'))
    print('~~'*20)
    if x in 'Nn':
        if preço>=1000.00:
            cont+=1
        if preço < menor:
            preço = menor
            nome=mp
        print (f'O total da compra é {soma:.2f}'
           f'temos {cont} produtos no valor acima de R$1000,00 '
            f' O produto mais barato é o {mp} com o valor de {menor}' )

        break
