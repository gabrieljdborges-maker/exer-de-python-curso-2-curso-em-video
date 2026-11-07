from math import floor

print('~~~~'*40)
while True:
    x=int(input('Quanto dinheiro você quer sacar ? R$'))
    cin=x/50
    vinte=(x%50)/20
    dez=((x%50)%20)/10
    um=(((x%50)%20)%10)/1
    print(f'Você irá receber {floor(cin):.0f} notas de R$50\nIrá receber {floor(vinte):.0f} notas de R$20\nIrá receber {floor(dez):.0f} notas de R$10\ne ira receber {floor(um):.0f} notas de R$ 1.')
    print('~~~~'*40)
    print(' Volte Sempre ao Banco ! tenha um bom dia ')
    break
