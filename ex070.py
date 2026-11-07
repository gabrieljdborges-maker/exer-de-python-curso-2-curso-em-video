soma=0
while True :
    preço=int(input('Informe o preço do Produto : '))
    nome=str(input('Informe o nome do Produto : '))
    soma+=preço
    menor=preço
    if preço < menor:
        preço=menor
    x=str(input('Quer cadastrar mais algum item ?'))
    print('~~'*20)
    if x in 'Nn':
        menu=str(input('MENU'
                       '\n[A] - Qual é o total gasto nessa Compra ?'
                       '\n[B] - Qual produto custa mais de R$ 1000,00 ? '
                       '\n[C] - Qual o nome do produto mais Barato ?'))
        if menu in 'Aa':
            print (soma)
        if menu in 'Bb':
                if preço>=1000:
                    print(nome)
                else:
                    print('Não temos produtos com este valor ou maior')
        if menu in 'Cc':
            print(menor)
        break