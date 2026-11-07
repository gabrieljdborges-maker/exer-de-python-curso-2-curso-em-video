p=int(input('Informe o valor do priemrio termo dessa PA: '))
r=int(input('Informe o valor da razão dessa PA: '))
t=int(input('Informe o valor do ultimo termo'))
d=1
i=1
while i==0 :
    d= p + (t - 1) * r
    i-=1
print ('O valor da PA com p1={}, com o R={} e com o {}º termo é {}'.format(p,r,t,d))
