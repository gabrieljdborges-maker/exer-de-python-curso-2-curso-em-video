from datetime import date

print('Estamos iniciando mais um programa do Governo O Alistamento Obrigatorio')
nome=str(input('Informe seu nome completo : ')).strip().title()
ano=int(input('Informe seu ano de Nascimento :'))
anoatual=date.today().year
x=abs(ano-anoatual)
if ano==anoatual:
    print(' {} acabou de nascer espere mais 18 anos !!'.format(nome))
    print('{} seu alistamento será em {}'.format(nome,anoatual+18))
elif x==18:
     print ('Chegou a hora de {} se alistar !!!!\n Va até o posto da União mais proximo da sua casa \n RG, comprovante de residencia !!!!'.format(nome))
elif x<18:
    alis=anoatual+abs(x-18)
    print ('{}, você ainda tem que aguardar {} anos para se alistar'.format((nome),abs(x-18)))
    print ('{} , seu alistamento será em {} '.format(nome,alis))
else:
    alis1=anoatual-abs(x-18)
    print('{} já se alistou a mais de {} anos '.format(nome,abs(x-18)))
    print('{} já seu alistamneto foi em {} '.format(nome,alis1))
