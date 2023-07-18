# identificação da loja e solicitação de entrada do valor e quantidade de produto.
print('Bem-vindo a Loja do Gabriel Costa Silva')
valor = float(input('Digite o valor unitário do produto: '))
quantidade = int(input('Digite a quantidade do produto: '))

if (quantidade < 200): # Verifica se a quantidade é menor que 200, se for verdadeiro nao se aplica desconto.
    print('O valor é: R$ {}'.format(valor * quantidade))
    print('Esta quantidade não se aplica desconto.')
elif (quantidade >= 200) and (quantidade < 1000): # Verifica se quantidade é maior ou igual que 200 e menor que 1000.
    desconto = (valor * quantidade) * (5/100) # Calcula o valor de 5% de desconto.
    print('O valor SEM desconto: R$ {}'.format(valor * quantidade)) # Mostra valor total sem desconto.
    print('O valor COM desconto: R$ {}'.format(valor * quantidade - desconto)) # Mostra valor total com desconto.
elif (quantidade >= 1000) and (quantidade < 2000):
    desconto = (valor * quantidade) * (10/100) # Calcula o valor de 10% de desconto.
    print('O valor SEM desconto: R$ {}'.format(valor * quantidade)) # Mostra valor total sem desconto.
    print('O valor COM desconto: R$ {}'.format(valor * quantidade - desconto)) # Mostra valor total com desconto.
elif (quantidade >= 2000):
    desconto = (valor * quantidade) * (15/100) # Calcula o valor de 15% de desconto.
    print('O valor SEM desconto: R$ {}'.format(valor * quantidade)) # Mostra valor total sem desconto.
    print('O valor COM desconto: R$ {}'.format(valor * quantidade - desconto)) # Mostra valor total com desconto.
else:
    print('Digite valores validos.') # Caso nenhuma condição seja atingida.
