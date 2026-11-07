print('~~' * 40)
while True :
    x=int(input('Qual a tabuada que você quer saber? (para encerrar informe um numero negativo) :'))
    if x<0:
        print('Fim do programa')
        print('~~' * 40)
        break
    else:
        print(f'{x} X 1 = {x*1}\n{x} X 2 = {x*2}\n{x} X 3 = {x*3}\n{x} X 4 = {x*4}\n{x} X 5 = {x*5}\n{x} X 6 = {x*6}\n{x} X 7 = {x*7}\n{x} x 8 = {x*8}\n{x} X 9 = {x*9}\n{x} X 10 = {x*10}')
        print('~~'*40)