nota = 8.5 # atribui o valor á variavel "nota".
disciplina = 'Logica de Programação e Algoritimos' # atribui uma string a variavel "disciplina".

print(nota) # imprime o valor que foi atribuido a variavel.
print(disciplina) # imprime o valor que foi atribuido a variavel.

print('Disciplina:',disciplina,'Nota:',nota) # concatenação de valores pre definidos nas respsctivas variaveis + strings que dao sentidos aos dados inseridos.

# uma variavel nao pode começar com numero, pode por no meio e no fim mais nao no inicio

# uma variavel pode ser por exemplo: 'nota5' ou '_n_o_t_a_' mais NÃO pode ser por exemplo: '5nota' ou '!nota'

# acima do python 3 é aceito acentuação, e outras linguagens nao aceita. Entao é melhor que nao seja utilizado para nao criar um mal vicio.

#----------------------------------------------------------------------------------------------------------------------------------------------------------

a = 1 # a recebe 1
b = 5 # b recebe 5

resposta = a == b
print(resposta) # ira comparar se a é igual a b e vai retornar um booleano (falso).

resposta = a != b
print(resposta) # ira comparar se a é diferente de b e vai retornar um booleano (verdadeiro).

frase = 'ola, mundo!'
print(frase)

print(frase[0]) # ira imprimir o indice 0 da frase, neste caso seria a letra "O"
print(frase[2]) # ira imprimir o indice 2 da frase, neste caso seria a letra "a"

# o indice começa com o primeiro elemento recebendo o valor de 0, por isso o primeiro resultado acima foi a letra "O"