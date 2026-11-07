while True:
    x=(int(input('Informe um numero: [NUM NEGATIVO ENCERRA O PROGRAMA]')))

    if x < 0:
        print('Programa Encerrado')
        break
    else :
        for c in range (1,11):
            print(f'{x} X {c} = {x*c}')
