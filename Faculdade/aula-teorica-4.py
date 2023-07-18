# ESTRUTURA DE REPETIÇÃO WHILE (EM QUANTO)

# REPETE UM BLOCO DE INSTRUÇÕES ENQUANTO DETERMINADA CONDIÇÃO SE MANTIVER VERDADEIRA,
# CASO CONTRÁRIO, OCORRE O DESVIO PARA A PRIMEIRA LINHA DE CÓDIGO APÓS ESTE BLOCO DE REPETIÇÃO.

x = 1
while ( x <= 5 ):
    print(x)
    x = x + 1 

# SE NAO HOUVER UM PARAMETRO LIMITE (VARIAVEL DE CONTROLE) NO CODIGO ELE ENTRARÁ EM UM LOOP INFINITO, PODENDO TRAVAR TANTO O
# PROGRAMA COMO O COMPUTADOR, UTILIZANDO TODA A MEMORIA. (STACK OVERFLOW).

#---- Exercicio com contador ----

# ESCREVA UM ALGORITMO QUE IMPRIMA NA TELA SOMENTE VALORES DENTRO DE UM INTERVALO ESPECIFICADO PELO USUARIO E QUE SEJAM NUMERO PARES.

inicial = int(input('Qual valor deseja iniciar a contagem? '))
final = int(input('Qual valor deseja encerrar a contagem? '))
x = inicial
while (x <= final):
    if (x % 2 == 0):
        print(x)
        x = x + 1

#---- Exercicio com acumulador ----

# ESCREVA UIM ALGORITMO QUE CALCULE A SUA MEDIA DE NOTAS EM DETERMINADA DISCIPLINA, VAMOS ASSUMIR QUE A MEDIA
# FINAL E DADA PELA MEDIA ARITMETICA DE CINCO NOTAS DIGITADAS.

soma = 0
cont = 1
while (cont <= 5):
    x = float(input('Digite a {}ª nota: '.format(cont)))
    soma = soma + x
    cont = cont + 1
media = soma / 5
print('Média final é: {}'.format(media))

# ---- VALIDANDO DADOS DE ENTRADA

# CRIE UM ALGORITMO QUE RECEBA UM VALOR DO TIPO INTEIRO VIA TECLADO
# NO ENTANTO, O PROGRAMA SO DEVE ACEITAR, OBRIGATORIAMENTE VALOS INTEIROS E POSITIVOS
# QUALQUER VALOR NEGATIVO, OU IGUAL A ZERO, DEVE SER REJEITADO PELO PROGRAMA E UM NOVO VALOR DEVFE SER SOLICITADO

# validando a entrada
x = int(input('Digite um valor maior do que zero: '))
while (x <= 0):
    x = int(input('Digite um valor maior do que zero: '))
print('Você digitou {}. Encerrando o programa...'.format(x))

# ESCREVA UM ALGORITMO QUE FIQUE RECEBENDO FRASES OU PALAVRAS DIGITADAS PELO USUARIO
# ENCERRE O ALGORITMO QUANDO A PALAVRA SAIR FOR DIGITADA

print('Digite uma mensagem que irei repetir para você! ')
print('Para encerrar escreva "sair".')
while True:
    texto = input('')
    print(texto)
    if texto == 'sair':
        break
print('Encerrando programa...')

# INSTRUÇÃO CONTINUE

# O COMANDO CONTINUE SERVE PARA RETORNAR O LAÇO AO INICIO A QUALQUER MOMENTO, INDEPENDENTEMENTE DO
# ESTADO DA VARIAVEL DE CONTROLE DA CONDICIONAL DO LAÇO.

# EXERCICIO:
# ESCREVA UM ALGORITMO QUE REALIZE UM LOGIN EM UM SISTEMA
# O USUARIO DEVE INFORMAR SEU NOME E SENHA.

while True:
    nome = input('Qual o seu nome? ')
    if (nome != 'gabriel'):
        continue
    senha = input('Qual a sua senha? ')
    if (senha == '1234'):
        break
print('Acesso concedido.')

# Valores Truthy e Falsey
# DADOS NAO BOOLEANOS TAMBEM PODEM SER TRATADOS COMO TRUE OU FALSE EM UMA CONDIÇÃO, SEJA ESTA UMA ESTRUTURA CONDICIONADA OU DE UM LAÇO

# - FALSEY / FALSE
#     NUMERO ZERO (INT OU FLOAT) E STRING VAZIA

# - TRUTHY / TRUE
#     QUALQUER OUTRO DADO

#EXEMPLO:

nome = ''
while not nome:
    nome = input('Digite seu nome: ')
valor = int(input('Digite um numero qualquer: '))
if valor:
    print('você digitou um valor diferente de zero.')
else:
    print('você digitou zero.')

# ESTRUTURA DE REPETIÇÃO FOR (PARA)

# ASSIM COMO O WHILE, ESSA ESTRUTURA REPETE UM BLOCO DE INSTRUÇÕES ENQUANTO UMA CONDIÇÃO SE MANTIVER VERADEIRA
# NO ENTANTO, DIFERENTEMENTE DO WHILE, O FOR É EMPREGADO EM SITUAÇÕES EM QUE O NUMERO DE VEZES QUE O LAÇO IRÁ EXECUTAR É FINITO E BEM DEFINIDO

for i in range(6): # 6 é o valor final do iterador
    print(i)

for i in range(1,6,1): # Para i no intervalo de 1 até 5 de passos de 1 em 1
    print(i)

for i in range(10, 0 -2): # Faz uma contagem decrescente de 10 até 0 pulando de 2 em 2 casas.
    print(i)

# EXERCICIO:
# ESCREVA UM ALGORITMO QUE CALCULE A MEDIA DOS NUMEROS PARES DE 1 ATE 100 (1 E 100 INCLUSOS).
# IMPLEMENTE O LAÇO USANDO FOR.

soma = 0
qtd = 0
for i in range(1,101):
    if (i % 2 == 0):
        soma += i 
        qtd += 1
media = soma / qtd
print('A media dos pares de 1 ate 100 é {}'.format(media))

# ESTRUTURAS DE REPETIÇÃO ANINHADAS

#EXERCICIO:
# ESCREVA UM ALGORITMO EM PYTHON QUE CALCULE A TABUADA DE TODOS OS NUMEROS DE 1 ATÉ 10, E PARA CADA NUMERO,
# VAMOS CALCULAR A TABUADA MULTIPLICANDO-O PELO INTERVALO DE 1 ATÉ 10

# 2 WHILE
tabuada = 1
while tabuada <= 10:
    print('TABUADA DO {}: ' .format(tabuada))
    i = 1
    while i <= 10:
        print('{} x {} = {}'.format(tabuada, 1, tabuada * i))
        i += 1
    tabuada += 1

# 2 FOR
for tabuada in range(1, 11, 1):
    print('TABUADA {}:'.format(tabuada))
    for i in range(1, 11, 1):
        print('{} x {} = {}'.format(tabuada, 1, tabuada * i))

# WHILE + FOR
tabuada = 1
while tabuada <= 10:
    print('TABUADA DO {}:'.format(tabuada))
    for i in range(1, 11, 1):
        print('{} x {} = {}'.format(tabuada, 1, tabuada * i))
    tabuada += 1