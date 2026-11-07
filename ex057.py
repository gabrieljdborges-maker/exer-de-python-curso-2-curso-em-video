x=''
while x!='M':
     x=str(input('informe seu sexo [M/F]')).strip().upper()
     if x=='M':
         print('Obrigado pela informação')
     elif x=='F':
        print('Obrigado pela informação')
        x='M'
     else:
       print('Você não seguiu o padrão solicitado, informe novamente')

