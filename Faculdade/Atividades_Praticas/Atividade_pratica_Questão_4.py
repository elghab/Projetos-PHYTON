# Define a variavel de id global e cria a lista de colaboradores que se inicia vazia.
lista_colaboradores = []
id_global = 0

# Função que cadastra um colaborador e adiciona seus respectivos dados
def cadastrar_colaborador(id):
    global id_global
    nome = input('Digite o nome do colaborador: ')
    setor = input('Digite o setor do colaborador: ')
    pagamento = float(input('Digite o pagamento do colaborador: '))

# Dicionario que armazena os dados do colaborador
    colaborador = { 
        "id": id,
        "nome": nome,
        "setor": setor,
        "pagamento": pagamento
    }

# Adiciona o Colaborador à lista de Colaboradores
    lista_colaboradores.append(colaborador)
    id_global += 1

# Função que consulta o colaborador, mostra todos, consulta por um valor de ID ou consulta por setor 
def consultar_colaborador():
    opcao = int(input("Qual opção deseja?\n1. Consultar Todos\n2. Consultar por Id\n3. Consultar por Setor\n4. Retornar ao menu\n"))
    
    if opcao == 1:
        for colaborador in lista_colaboradores:
            print(colaborador)
    elif opcao == 2:
        id_colaborador = int(input("Digite o ID do colaborador: "))
        for colaborador in lista_colaboradores:
            if colaborador["id"] == id_colaborador:
                print(colaborador)
    elif opcao == 3:
        setor_colaborador = input("Digite o setor do colaborador: ")
        for colaborador in lista_colaboradores:
            if colaborador["setor"] == setor_colaborador:
                print(colaborador)
    elif opcao == 4:
        return
    else:
        print("Opção inválida")

#Função que remove um colaborador da lista
def remover_colaborador():
    id_colaborador = int(input("Digite o ID do colaborador a ser removido: "))
    for colaborador in lista_colaboradores:
        if colaborador["id"] == id_colaborador:
            lista_colaboradores.remove(colaborador)
            print("Colaborador removido com sucesso.")
            return
    print("Colaborador não encontrado.")

#função inicial do programa
def main():
    print("Bem-vindo ao Software de Gerenciamento de Pessoas do Gabriel Costa Silva")

    while True:
        opcao = int(input("Escolha uma opção:\n1. Cadastrar Colaborador\n2. Consultar Colaborador\n3. Remover Colaborador\n4. Encerrar Programa\n"))

        if opcao == 1:
            cadastrar_colaborador(id_global)
        elif opcao == 2:
            consultar_colaborador()
        elif opcao == 3:
            remover_colaborador()
        elif opcao == 4:
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida")

main()
