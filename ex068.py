from random import randint
v=soma=0
print('~-~'*40)
print('JOGO DE PAR OU IMPAR')
while True :
    x=int(input('Digite um valor :'))
    y=randint(0,10)
    p=str(input('A soma dará PAR ou IMPAR ? [I/P]')).strip().upper()[0]
    soma=x+y
    par=soma%2
    if par == 0 :
        if p=='P':
            v+=1
            print('-=-='*40)
            print(f'\033[34mPARABENS !! VOCÊ VENCEU!!! \nEscolheu {x} o PC escolheu {y}.Total é {soma} que deu PAR ')
            print('-=-=' * 40)
        elif p!='P':
            if v==0:
                print('\033[31mVocê não venceu nenhuma :(')
                break
            else:
                print('-=-=' * 40)
                print(f'\033[31mEssa você perdeu, pois a soma de {x} e {y} deu {soma}, que é PAR\nMas já ganhou {v} vezes')
                break
    else :
        if p=='I':
            v+=1
            print('-=-=' * 40)
            print(f'\033[34mPARABENS !! VOCÊ VENCEU!!! \nEscolheu {x} o PC escolheu {y}.Total é {soma} que deu IMPAR ')
            print('-=-=' * 40)
        elif p!='I':
            if v==0:
                print('\033[31mVocê não venceu nenhuma :(')
                break
            else:
                print('-=-=' * 40)
                print(f'\033[31mEssa você perdeu, pois a soma de {x} e {y} deu {soma}, que é IMPAR\nMas já ganhou {v} vezes')
                break
