media=[]
maioridadehomem=0
nomevelho=''
idademulher=0
menorde20=0
for x in range(1,6):
    print('-'*20,'{} Pessoa'.format(x),'-'*20)
    nome=str(input('Qual é o Nome da {}º pessoa ? '.format(x))).strip().lower()
    idade=int(input('Qual a idade da {}º pessoa?'. format(x)))
    sexo=str(input('Qual é o Sexo da {}º pessoa ?[M/F]'.format(x))).strip().lower()
    media.append(idade)
    if x==1 and sexo =='m':
        maioridadehomem=idade
        nomevelho=nome
    if sexo =='m'and idade> maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo =='f' and idade<20:
        menorde20+=1
divi=int((sum(media))/5)
print ('A média de idade das {} pessoas é de {}'.format(x,divi))
print('O homem é o {} mais velho tem {} anos '.format( nomevelho,maioridadehomem))
print('Nessa pesquisa tivemos {} mulheres menores de 20 anos'.format(menorde20))
