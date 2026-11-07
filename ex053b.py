frase=str(input('informe sua frase')).strip().upper()
s=frase.split()
junto=''.join(s)
inversa=''
for letra in range(len(junto)-1,-1,-1):
    inversa+=junto[letra]
if inversa==junto:
       print ('A frase é um políndromo pois {} é igual a {}'.format(junto,inversa))
else:
       print ('A frase não é um polindromo pois {} não é gual a {}'.format(junto,inversa))
