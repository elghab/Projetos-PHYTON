
print('Bem-vindo a Sorveteria do Gabriel Costa Silva')
print(38 * '-' + 'Cardápio' + 38 * '-')
print('| N.º DE BOLAS | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es) |')
print('|' + 7 * ' ' + '1' + 6 * ' ' + '|' + 9 * ' ' + 'R$ 6,00' +  8 * ' ' + '|'+ 6 * ' ' + 'R$ 7,00' +  7 * ' ' + '|'+ 7 * ' ' + 'R$ 8,00' +  7 * ' ' + '|')
print('|' + 7 * ' ' + '2' + 6 * ' ' + '|' + 9 * ' ' + 'R$ 11,00' +  7 * ' ' + '|'+ 6 * ' ' + 'R$ 13,00' +  6 * ' ' + '|'+ 7 * ' ' + 'R$ 15,00' +  6 * ' ' + '|')
print('|' + 7 * ' ' + '3' + 6 * ' ' + '|' + 9 * ' ' + 'R$ 15,00' +  7 * ' ' + '|'+ 6 * ' ' + 'R$ 18,00' +  6 * ' ' + '|'+ 7 * ' ' + 'R$ 21,00' +  6 * ' ' + '|')
print(84 * '-')

total = 0 # Inicia o valor a ser pago como R$ 00,00 para ser adicionado mais à frente

while True:
    # Solicita o sabor desejado, e atribui o nome completo à abreviação
    sabor = input('Entre com o sabor desejado (tr/es/pr): ')
    if sabor == 'tr':
        sabor = 'TRADICIONAL'
    elif sabor == 'es':
        sabor = 'ESPECIAL'
    elif sabor == 'pr':
        sabor = 'PREMIUM'
    else:
        print('Sabor inválido. Tente novamente') # Caso o sabor seja inválido, re-inicia o loop
        continue

    # Solicita a quantidade de bolas de sorvete.
    qtd_bolas = input('Entre com o número de bolas de sorvete desejado (1/2/3): ')
    if qtd_bolas != '1' and qtd_bolas != '2' and qtd_bolas != '3': # Verifica se o valor digitado é diferente do pré-definido. Se for o caso re-inicia o loop a partir do número de bolas de sorvete
        print('Número de bolas de sorvete inválido. Tente novamente')
        continue
    
    # Faz o cálculo do valor do sorvete de acordo com o sabor que foi selecionado e a quantidade de bolas
    valor_sorvete = 0 

    if sabor == 'TRADICIONAL':
        if qtd_bolas == '1':
            valor_sorvete = 6
        elif qtd_bolas == '2':
            valor_sorvete = 11
        elif qtd_bolas == '3':
            valor_sorvete = 15

    elif sabor == 'PREMIUM':
        if qtd_bolas == '1':
            valor_sorvete = 7
        elif qtd_bolas == '2':
            valor_sorvete = 13
        elif qtd_bolas == '3':
            valor_sorvete = 18

    elif sabor == 'ESPECIAL':
        if qtd_bolas == '1':
            valor_sorvete = 8
        elif qtd_bolas == '2':
            valor_sorvete = 15
        elif qtd_bolas == '3':
            valor_sorvete = 21

    print('Você pediu {} bola(s) de sorvete no sabor {}: R$ {:.2f}'.format(qtd_bolas, sabor, valor_sorvete))  # Exibe o pedido atual com o valor do sorvete em específico

    total += valor_sorvete  # Atualiza o total com o valor do sorvete do pedido atual

    while True: # faz uma verificação no final de cada pedido para saber se deve ou não continuar
        resposta = input('Deseja pedir mais alguma coisa? (s/n): ')
        if resposta == 's': # Sai do loop e volta para o início do loop principal para solicitar um novo pedido
            break
        elif resposta == 'n':
            print('Valor total a pagar: R$ {:.2f}'.format(total)) # Formata a string de saída e exibe o valor total a pagar formatado com duas casas decimais
            break
        else:
            print('Resposta inválida. Tente novamente.')
            continue

    if resposta == 'n':
        break