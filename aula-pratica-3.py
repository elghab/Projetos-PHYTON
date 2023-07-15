#ESCREVA AS SEGUINTES EXPRESSOES BOOLEANAS EM LINGUAGEM PYTHON:

# A ) O somatorio de 2 com 2 é menor do que 4
print(2 + 2 < 4)

# B ) O valor 7 // 3 é igual a 1 + 1
print(7 // 3 == 1 + 1)

# C ) A soma de 3 elevado ao quadrado com 4 elevado ao quadrado é igual a 25
print(3**2 + 4**2 == 25)

# D ) A soma de 2, 4 e 6 é maior do que 12
print(2 + 4 + 6 > 12)

# E ) 1387 é divisivel por 19
print(1387 % 19 == 0)

# F ) 31 é par
print(31 % 2 == 0)

# G ) O menor valor entre: 34,29 e 31 é menor do que 30
print( 34,29 / 31 < 30)

#--------------------------------------------------------------------------

# TRADUZA AS AFIRMAÇÕES A SEGUIR PARA CONDICIONAIS EM PYTHON

# A ) Se idade é maior que 60, escreva: "Você tem direitos aos beneficios"
if (idade > 60):
    print('você tem direito aos beneficios!')

# B ) Se dano é maior do quie 10 e escudo é igual a 0, escreva: "Você está morto"
if (dano > 10 and escudo == 0):
    print('Você está morto!')
    
# C ) Se pelo menos uma das variaveis booleanas norte, sul, leste e oeste resultarem em True, escreva: "Você escapou!"
if (norte or sul or leste or oeste):
    print('Você escapou! ')

# D ) Se ano é divisivel por 4, escreva: "Pode ser um ano bissexto". Caso contrário, escreva: "Definitivamente nao é um ano bissexto"
ano = 2023
if (ano % 4 == 0):
    print('O ano pode ser bissexto!')
else:
    print('Definitivamente nao é um ano bissexto')

# E ) Se ambas as variaveis booleanas cima e baixo rorem True, escreva: "Decida-se!", caso contrário, escreva: "Você escolheu um caminho!"
cima = True
baixo = True
if (cima and baixo):
    print('Decida-se!')
else:
    print('Você escolheu um caminho!')

#------------------------------------------------------------------------------

# FAÇA UM ALGORITIMO EM QUE RECEBA TRES VALORES, REPRESENTANDO OS LADOS DE UM TRIANGULO FORNECIDOS PELO USUARIO. 
# VERIFIQUE SE OS VALORES FORMAN UM TRIANGULO E CLASSIFIQUE COMO:

#       LEMBRE-SE DE QUE, PARA FORMAR UM TRIÂNGULO, NENHUM DOS LADOS PODE SER IGUAL A ZERO, E UM LADO NAO PODE SER MAIOR QUE A 
#       SOMA DOS OUTROS DOIS (EXERCICIO DA APOSTILA - AULA 3)

# A ) Equilátero (três lados iguais)
# B ) Isósceles (dois lados iguais)
# C ) Escaleno (três lados diferentes)

A = int(input('Digite o 1* lado do triangulo'))
B = int(input('Digite o 2* lado do triangulo'))
C = int(input('Digite o 3* lado do triangulo'))

if (A > 0) and (B > 0) and (C >0):
    if (A + B > C) and (A + C > B) and (B + C > A):
    # A partir daqui ja foi verificado se é um triangulo valido e irá fazer a verificação do tipo do triangulo.
        if A != B and A != C and B != C:
            print('Triangulo escaleno')
        else:
            if A == B and A == C and B == C:
                print('Triangulo equilatero!')
            else:
                print('Triangulo isoceles!')
    else:
        print('Ao menos um dos valores  indicados nao servem para formar um triangulo')
else:
    print('Ao menos um dos valores  indicados nao servem para formar um triangulo')
