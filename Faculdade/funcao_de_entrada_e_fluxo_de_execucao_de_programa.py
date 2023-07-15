# input é utilizado quando queremos que aconteça uma entrada de dados como nos exemploas abaixo onde é feito uma pergunta e o programa fica esperando 
# voce digitar uma resposta e somente apos isso que sera printado no console o que voce digitou

idade = input('Qual sua Idade?')
print(idade) # o valor que for digitado no console sera o valor atribuido a variavel idade.

nome = input('Qual seu nome?')
print('ola {}, seja bem-vindo!'.format(nome))

# uma observação muito importante é que todos os valores recebidos atraves do input é do tipo string e caso queira trabalhar com esse input como numero
# é necessario fazer uma converção deste valor como no exemplo abaixo, utilizando o tipo antes do input.

nota = float(input('Qual nota voce recebeu na disciplina?'))
print('Voce tirou nota {}.'.format(nota))

#--

# Exercicio 2.1
x = int(input('Digite o primeiro numero:'))
y = int(input('Digite o segundo numero:'))
# Maneira Classica
res = 'O resultado da soma de %i com %i é %i' % (x, y, x + y)
# Maneira Moderna
res = 'O resultado da soma de {} com {} é {}' .format(x, y, x + y)
print(res)