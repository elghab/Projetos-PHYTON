#Lê dois valors inteiros e compara ambos
x = int(input('Digite um valor inteiro'))
y = int(input('Digite um segundo valor inteiro'))
if (x>y):
    print('O primeiro valor é maior que o segundo!')

#--

#par ou ímpar
x = int(input('Digite um valor inteiro: '))
if (x % 2 == 0):
    print('O número é par!')
else:
    print('O número é impar!')

# exercicio ---
print('Escolha o que deseja comparar:')
print('1 - Maça')
print('2 - laranja')
print('3 - banana')
produto = int(input('Qual sua escolha?'))
qtd = int(input('quantas unidades?'))
if (produto == 1):
    pagar = qtd *2.3
    print('Você comprou {} maças. Total a pagar: {}'.format(qtd, pagar))
else:
    if (produto == 2):
        pagar = qtd *3.6
        print('Você comprou {} laranjas. Total a pagar: {}'.format(qtd, pagar))
    else:
        if (produto == 3):
            pagar = qtd *1.85
            print('Você comprou {} bananas. Total a pagar: {}'.format(qtd, pagar))
        else:
            print('Produto inexiste!')


# --- o mesmo exemplo do exercicio de cima so que usando o elif para simplificar.
print('Escolha o que deseja comparar:')
print('1 - Maça')
print('2 - laranja')
print('3 - banana')
produto = int(input('Qual sua escolha?'))
qtd = int(input('quantas unidades?'))
if (produto == 1):
    pagar = qtd *2.3
    print('Você comprou {} maças. Total a pagar: {}'.format(qtd, pagar))
elif (produto == 2):
    pagar = qtd *3.6
    print('Você comprou {} laranjas. Total a pagar: {}'.format(qtd, pagar))
elif (produto == 3):
    pagar = qtd *1.85
    print('Você comprou {} bananas. Total a pagar: {}'.format(qtd, pagar))
else:
    print('Produto inexiste!')