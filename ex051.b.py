p=int(input('Informe o primeiro termo de uma PA:'))
r=int(input('Informe a razão de uma PA '))
trin=p+(10-1)*r
termo=0
for x in range(p,trin+r,r):
    termo+=1
    print ('O {}ºtermo é {}\n'  .format(termo,x), end= '')