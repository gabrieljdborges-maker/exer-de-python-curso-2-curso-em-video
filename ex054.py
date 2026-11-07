from datetime import date
x=date.today().year
cont=0
cont2=0
for ano in range (1,8):
       ano=int(input('Qual é seu ano de nascimento ?'))
       if abs(ano - x) >= 18:
           cont+=1
       else:
            cont2+=1
print ('Ao todo tivemos  {} maiores de idade \n e também tivemos  {} menores de idade'.format(cont,cont2))
