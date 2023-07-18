def cachorro_peso(): # Define uma função que recebe o valor do peso, valida se é aceitavel e retorna o valor para a variavel de acordo com o peso 
    while True:
        try:
            peso = float(input("Qual é o peso do cachorro? "))
            if peso >= 50:
                print("Não aceitamos cachorros tão grandes.")
            elif peso < 3:
                return 40
            elif peso >= 3 and peso < 10:
                return 50
            elif peso >= 10 and peso < 30:
                return 60
            elif peso >= 30 and peso < 50:
                return 70
        except ValueError: # Em caso de nao digitar um numero, reconhece a exceção e mostra uma mensagem dizendo o que deve ser feito
            print("Por favor, digite um valor numerico para o peso.")

def cachorro_pelo(): # Define uma função que pergunta ao usuario qual o tipo de pelo do cachorro, e atribui um multiplicador.
    while True:
        print(' ')
        print('Qual é o tipo de pelo do cachorro?')
        print('c - curto')
        print('m - médio')
        print('l - longo')
        pelo = input('>> ')
        if pelo == 'c':
            return 1
        elif pelo == 'm':
            return 1.5
        elif pelo == 'l':
            return 2
        else:
            print("Opção inválida. Digite 'c' para pelo curto, 'm' para pelo médio ou 'l' para pelo longo.") # Em caso de resposta errada, diz ao usuario o que deve ser escolhido.

def cachorro_extra(): # Cria uma função que verifica os serviços extras 
    total_extra = 0 # de inicio o valor total dos serviços extras é definido como 0
    while True: # cria um laço infinito onde repetirá a pergunta até a opção ser 0, e toda excolha de serviço extra tem seu valor adicionado na variavel total_extra acima.
        print(' ')
        print('Deseja adicionar algum serviço extra?')
        print('1 - cortar unhas')
        print('2 - escovar dentes')
        print('3 - limpar orelhas')
        print('0 - não desejo mais nada')
        extra = input(">> ")
        if extra == '0':
            return total_extra
        elif extra == '1':
            total_extra += 10
        elif extra == '2':
            total_extra += 12
        elif extra == '3':
            total_extra += 15
        else:
            print("Opção inválida. Digite '1' para cortar unhas, '2' para escovar dentes, '3' para limpar orelhas ou '0' para não querer mais nada.")# Em caso de resposta errada, diz ao usuario o que deve ser escolhido.

def main(): # Define a função do programa que é iniciada, recebe os valores após serem validados e faz o calculo do valor total
    print("Bem-vindo ao Petshop do Gabriel Costa Silva")
    nome = input("Por favor, digite o seu nome: ")
    print("Olá,", nome)

    try:
        peso = cachorro_peso()

        pelo = cachorro_pelo()

        extras = cachorro_extra()
        
        total = peso * pelo + extras
        print(' ')
        print('Total a pagar: R$ {:.2f} (peso: {} * pelo: {} + adicional(is): {})'.format(total, peso, pelo, extras)) #Trás o valor a ser pago e o calculo que foi feito.
    except ValueError: # Em caso de nao digitar um numero na função de peso, reconhece a exceção e mostra uma mensagem dizendo o que deve ser feito
        print("Por favor, digite um valor numérico para o peso.")

main()