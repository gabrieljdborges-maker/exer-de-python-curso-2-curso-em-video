from time import sleep as s
print ('-=-='*30)
print (' Neste Programa iremos calcular se IMC utilizando seu peso e altura')
print ('-=-='*20)
nome=str(input('Qual seu nome ? ')).strip().title()
s(3)
altura=float(input('Qual sua altura  ?'))
s(3)
peso=float(input('Qual é seu peso ?'))
s(3)
imc=peso/(pow(altura,2))
if imc <= 18.5:
    print('Olá {} seu Imc está em {} , fale com um médico'.format(nome,imc))
if imc > 18.5 and imc <= 25.0:
    print('Olá {} seu Imc está em {}, está com o peso ideal'.format(nome,imc))
if imc > 25 and imc <=30.0:
    print('Olá {} seu Imc está em {}, está acima do peso, entre em contato com um Nutri'.format(nome,imc))
if imc > 30 and imc<= 40.0:
    print ('Olá {} , seu Imc está em {}, está em obesidade , vá num médico '.format (nome,imc))
else:
    print ('olá seu Imc está em {}, está com obesidade morbida, vá urgente a um médico'.format (nome,imc))
