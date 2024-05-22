def adicionar_contato(list_contatos, nome_contato, telefone_contato, email_contato):

  # tarefa: nome da tarefa
  # completada: indicar se essa tarefa ja foi completada ou nao
  contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": False}
  list_contatos.append(contato)
  print(f"\nContato {nome_contato} foi adicionado com sucesso!")
  return

def ver_contatos(list_contatos):
  print("\nLista de Contatos:")

  for indice, contato in enumerate(list_contatos, start=1):
      status = "✓" if contato["favorito"] else " "
      nome = contato["nome"]
      telefone = contato["telefone"]
      email = contato['email']
      print(f"{indice}. [{status}] {nome}, telefone: {telefone} e email: {email}")
  return

def editar_contato(list_contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(list_contatos):
      
    while True:
        print("\nEscolha o que deseja editar:")
        print("1. Editar nome")
        print("2. Editar telefone")
        print("3. Editar email")
        print("4. Sair")
        escolha = input("Digite a sua escolha: ")
        if escolha == "1":
            novo_nome = input("Digite o novo nome do contato: ")
            list_contatos[indice_contato_ajustado]['nome_contato'] = novo_nome
            print(list_contatos[indice_contato_ajustado]['nome_contato'])      

        elif escolha == "2":
            novo_telefone = input("Digite o novo telefone do contato: ")
            list_contatos[indice_contato_ajustado]["telefone_contato"] = novo_telefone
                    
        elif escolha == "3":
            novo_email = input("Digite o novo email do contato: ")
            list_contatos[indice_contato_ajustado]["email_contato"] = novo_email         
                    
        elif escolha == "4":
            break

        else:
            print("Escolha inválida. Tente novamente.")
                   
        print("O contato foi editado com sucesso!")
  else:
      print("Índice de contato inválido.")
  return list_contatos

def favoritar_contato(list_contatos, indice_contato):
    list_contatos[int(indice_contato) - 1]["favorito"] = True
    print("\nContato marcado como favorito com sucesso!")
    return

def visualizar_favoritos(list_contatos):
  for indice, contato in enumerate(list_contatos):
      if contato["favorito"]:
          status = "✓"        
          nome = contato["nome"]
          telefone = contato["telefone"]
          email = contato['email']
          print(f"\n{indice}. [{status}] {nome}, telefone: {telefone} e email: {email}")
  return

def deletar_contato(list_contatos, indice_contato):
  del list_contatos[int(indice_contato) - 1]
  print("\nContato deletado com sucesso!")
  return

list_contatos = []

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
        nome_contato = input("Digite o nome do contato que deseja adicionar: ")
        telefone_contato = input("Digite o telefone do contato que deseja adicionar: ")
        email_contato = input("Digite o email do contato que deseja adicionar: ")
        adicionar_contato(list_contatos, nome_contato, telefone_contato, email_contato)


    elif escolha == "2":
        ver_contatos(list_contatos)

    elif escolha == "3":
      ver_contatos(list_contatos)
      indice_contato = input("Digite o número do contato que deseja editar: ")
              
      list_contatos = editar_contato(list_contatos, indice_contato)
    
    elif escolha == "4":
        ver_contatos(list_contatos)
        indice_contato = input("Digite o número do contato que deseja marcar como favorito: ")
    
        favoritar_contato(list_contatos, indice_contato)
    
    elif escolha == "5":
        
        visualizar_favoritos(list_contatos)

    elif escolha == "6":
        ver_contatos(list_contatos)
        deletar = input("Digite o número do contato que deseja deletar: ")
        deletar_contato(list_contatos, deletar)

    elif escolha == "7":
        break

print("Programa finalizado")
