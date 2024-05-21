contatos = {}
while True:
    print("\nMenu do Gerenciador de Lista de Contatos:")
    print("1. Adicionar contato")
    print("2. Visualizar Contatos")
    print("3. Editar Contatos")
    print("4. Favoritar Contatos")
    print("5. Visualizar favoritos")
    print("6. Deletar Contatos")
    print("7. Sair")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        contatos["Nome"] = input("Digite o nome do contato que deseja adicionar: ")
        contatos["Telefone"] = input("Digite o telefone do contato que deseja adicionar: ")
        contatos["Email"] = input("Digite o email do contato que deseja adicionar: ")
        contatos["favorito"] = False

    elif escolha == "2":
        print(contatos)

    elif escolha == "3":
        nome = input("Digite o nome do contato que deseja editar: ")

    elif escolha == "7":
        break

print("Programa finalizado")
