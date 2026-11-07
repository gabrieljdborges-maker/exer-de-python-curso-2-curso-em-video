from time import sleep

print('Olá este é o analisador de crédito Bancario . Aguarde alguns segundos ')
sleep(4)
nome=str(input('Poderia informar seu nome ? ')).strip().capitalize()
sleep(4)
entrada=float(input('Poderia informar o valor da entrada? caso não tenha digite 0 '))
sleep(4)
s1=float(input('Para nossa analise precisamos que informe seu salario : '))
sleep(4)
vc=float(input('Poderia informar o valor da casa que quer comprar : '))
sleep(4)
anos=int(input('Em quantos anos você deseja pagar este imovel ? '))
par=(vc-entrada)/(anos*12)
if par>s1*(30/100):
    print (' {}, Infelizmente o seu emprestimo não foi aceito '.format(nome))
else:
    print('Sr(a){} o financiamento foi aprovado!! \n O valor da parecela mensal é de {:.2f}'.format (nome,par))
