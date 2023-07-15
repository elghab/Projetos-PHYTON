s1 = 'Logica de Programação'
s1 = s1 + 'e Algoritimos'
print(s1)

# o que acontece acima é que foi definido uma variavel e depois foi pego a mesma variavele e a concatenando com outra.
# fazendo com que o resultado seja impresso "Logica de programação e Algoritimos"

#--

s1 = 'A' + '-' * 10 + 'B'
print(s1) # Neste exemplo, o '-' seria multiplicado por 10 e todo o resto sera concatenado, imprimindo entao no console "A----------B"

#--

nota = 8.5
s1 = 'Voce tirou %f na disciplina de Algoritmos' % nota
print(s1)

# o "%f" que aparece no meio da string acima sera substituido por o que for definido do lado de fora da string (o f significa que é do tipo Float) com um sinal de % seguido da variavel
# no caso ali seria o nota entao resultaria no console em "Voce tirou 8.500000 na disciplina de Algoritmos"

#--

nota = 8.5
s1 = 'Voce tirou %.2f na disciplina de Algoritmos' % nota
print(s1)

# o "%f" que aparece no meio da string acima fará o mesmo que no exemplo acima, o diferencial é que será delimitado o numero de casas decimais para apenas 2 casas apos a virgula.
# no caso ali seria o valor de nota entao resultaria no console em "Voce tirou 8.500000 na disciplina de Algoritmos" e agora com essa modificação aparecerá apenas 
# "Voce tirou 8.50 na disciplina de Algoritmos".

#--

nota = 8.5
disciplina = 'Algoritmos'
s1 = 'Voce tirou %.2f na disciplina de %s ' % (nota, disciplina)
print(s1)

# o %s significa o mesmo que o do exemplo anterior mais agora é referente ao tipo string
# no final agora por ter mais de uma variavel é colocado entre parentese, uma observação 
# é que dentro do parentese é colocado as variaveis na ordem que aparece as modificações no codigo.


    #Lista de marcadores de posição
#-----------------------------------------
# Marcador | Tipo                        -
# %d ou %i | Números inteiros            -
# %f       | Números de ponto flutuante  -
# %s       | Strings                     -
#-----------------------------------------

# uma composicao mais moderna seria fazer assim:

nota = 8.5
disciplina = 'Algoritmos'
s1 = 'voce tirou {} na disciplina de {}'.format(nota, disciplina)
print(s1)

# podemos fatiar uma string usando a ideia dos indices:

s1 = 'Lógica de Programação e Algoritmos'
print(s1[0:6])
#Lógica (sempre ira imprimir ate um numero a menos que o maximo colocado para a impressao (5 neste caso))

s1 = 'Lógica de Programação e Algoritmos'
print(s1[24:34])
#Algoritmos

s1 = 'Lógica de Programação e Algoritmos'
print(s1[:6])
#Lógica (nao é necessario colocar um valor para iniciar caso seja naturalmente 0 o primeiro valor)

#--

s1 = 'Logica de Programação e Algoritmos'
tamanho = len(s1)
print(tamanho)

# o len irá contar quantos caracteres tem a string neste caso o resultado impresso seria "34"
