# ESCREVA AS SEGUINTES EXPRESSÕES ALGEBRICAS EM LINGUAGEM PYTHON:

# A) O somatório dos 5 primeiros números inteiros e poositivos
1 + 2 + 3 + 4 + 5

# B) A média entre 23, 19 e 31
(23+19+31)/3

# C) O número de vezes que 73 cabe em 403
403 // 73

# D) A sobra quando 403 é dividido por 73 
403 % 73

# E) 2 elevado à 10^ potencia
2**10

# F) O valor absoluto da diferenca entre 54 e 57
abs(54-57)

# G) O menor valor entre 34, 29 e 31
min(34, 29, 31)

#-------------------------------------------------------------------------------

# ESCREVA AS EXPRESSOES EM PYTHON PARA:

# A) Atribuir o valor inteiro à variavel a
a = 3

# B) Atribuir o valor 4 à variavel b
b = 4

# C) Atribuir à variavel c o valor da expressão a*a + b*b
c = a*a+b*b

#-------------------------------------------------------------------------------

# EXECUTE AS SEGUINTES ATRIBUIÇÕES:

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

# AGORA, UTILIZANDO OPERADORES + E *, CRIE AS SAÍDAS A SEGUIR:

# A) 'ant bat cod'
print(s1 + ' ' + s2 + ' ' + s3)

# B) 'ant ant ant ant ant ant ant ant ant ant'
print(10 * (s1 + ' '))

# C) 'ant bat bat cod cod cod'
print(s1 + ' ' + (2*(s2 + ' ') + (3*(s3 + ' '))))

# D) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
print(7*(s1 + ' ' + s2 + ' '))

# E) 'batbatcod batbatcod batbatcod batbatcod batbatcod'
print(5*(2*s2+s3 + ' '))

#-------------------------------------------------------------------------------

# DESENVOLVA UM ALGORITMO QUE SOLICITE AO USUARIO O PRECO DE UM PRODUTO E UM PERCENTUAL DE DESCONTO A SER APLICADO A ELE. 
# CALCULE E EXIBA O VALOR DO DESCONTO E O PRECO FINAL DO PRODUTO (EXERCICIO DA APOSTILA - AULA 2)

preco = float(input('Digite o preco do produto:'))
p = float(input('Digite o percentual de desconto (0-100)%:'))

desconto = preco * (p / 100)
final = preco - desconto

print('O preco do produto é {}. Desconto de {}%.'.format(preco, p))
print('Valor calculado de desconto: {}. Valor final do produto: {}'.format(desconto, final))

# ESCREVA MUM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO PELO USUÁRIO, ASSIM COMO A QUANTIDADE DE DIAS
# PELOS QUAIS O CARRO FOI ALUGADO. CALCULE O PRECO A PAGAR, SABENDO QUE O CARRO CUSTA R$ 60 POR DIA E R$ 0,15 POR KM RODADO.

km = int(input('Quantos km foram percorridos?'))
dias = int(input('Quantos dias ele foi alugado?'))

preco = 60 * dias + 0.15 * km

print('km = {}. Dias: {}'.format(km, dias))
print('Valor a ser pago: {}'.format(preco))

# CRIE UMA VARIAVEL DE STRING QUE RECEBA UMA FRASE QUALQUER. CRIE UMA SEGUNDA VARIAVEL, AGORA CONTENDO A METADE DA STRING DIGITADA.
# IMPRIMA NA TELA SOMENTE OS DOIS ULTIMOS CARACTERES DA SEGUNDA VARIAVEL DO TIPO STRING.

frase = input('Digite uma frase')
tam = len(frase)

frase2 = frase[:int(tam/2)]

print(frase2[-2:])