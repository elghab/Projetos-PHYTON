print ('ola mundo') # Imprime o texto strig "Ola mundo".
print (2+3) # soma os dois numeros inteiros 2+3=5.
print ('2'+2) # aconteçe um erro pois nao é possivel somar uma string com um inteiro.
print ('3+5') # irá escrever no console em string "3+5" e nao fazer a soma pois estando entre aspas significa que e uma string e nao inteiro.
print ('3'+'3') # ira concatenar as duas strings, printando no console (em string) "33".
print ('Ola' + 'Mundo') # ira fazer a mesma coisa do de cima, so que agora sao duas strings que serao concatenadas.
print ('O resultado da soma de 2 + 3 é:', 2+3) # ira fazer uma concatenaçao do texto com o resultado de uma soma.

#------------------------------------------------------------------------------------------------------------------------------------------------

                                        #atenção à ordem de precedência dos operadores

print (10*(5+7)/4) # Aqui o resultado é 30, pois primeiro ele soma, depois ele divide o valor da soma e apos isso ele multiplica por 10.
print (10*(5+7/4)) # Aqui o resultado é 67.5 pois primeiro é feito a divisao, apos isso ele soma e só então é feito a multiplicação.
