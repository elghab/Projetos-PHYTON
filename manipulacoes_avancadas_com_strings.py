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

# o "%f" que aparece no meio da string acima sera substituido por o que for definido do lado de fora da string com um sinal de % seguido da variavel
# no caso ali seria o nota entao resultaria no console em "Voce tirou 8.500000 na disciplina de Algoritmos"

#--

nota = 8.5
s1 = 'Voce tirou %.2f na disciplina de Algoritmos' % nota
print(s1)

# o "%f" que aparece no meio da string acima fará o mesmo que no exemplo acima, o diferencial é que será delimitado o numero de casas decimais para apenas 2 casas apos a virgula.
# no caso ali seria o valor de nota entao resultaria no console em "Voce tirou 8.500000 na disciplina de Algoritmos" e agora com essa modificação aparecerá apenas 
# "Voce tirou 8.50 na disciplina de Algoritmos"

