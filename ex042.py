from time import sleep as s
print ('-=-'*30)
print('Neste programa iremos calcular se o triangulo existe ou não e Qual é seu tipo')
print ('-=-'*30)
s(3)
a=float(input('informe o lado a :'))
b=float(input('Informe o lado b :'))
c=float(input('informe o lado c :'))
s(3)
if a+b>c and b+c>a and a+c>b:
    print( 'é um triangulo!!\n', end ='')

    if a==b==c:
           print ('Equilatero ')
    elif  a==b!=c or a==c!=b or b==c!=a :
           print ('Isosceles')
    elif a!=b!=c:
            print ('Escaleno ')
else :
    print (' Não é um triangulo')
