def menuLista(tarefa):
    while True:
        menu = ("\nMENU\n"
                "1 - Mostrar Tarefas\n"
                "2 - Inserir Tarefa\n"
                "3 - Deletar Tarefa\n"
                "4 - Sair")
        print(menu)
        perguntaTarefa = input("Escolha uma opção: ")
        opcao = perguntaTarefa

        adicionarLista(tarefa, opcao)
        mostraLista(tarefa, opcao)
        deletarLista(tarefa, opcao)
        print("-"*60)
        if perguntaTarefa == "4":
            break

def adicionarLista (tarefa, opcao):
    if opcao == "2":
        tarefa.append(input("Qual a sua tarefa ? "))

def mostraLista (tarefa, opcao):
    if opcao == "1":
        if len (tarefa) == 0:
            print("A lista está vazia")
        else:
            for i in tarefa:
                print(f"- {i}")

def deletarLista (tarefa, opcao):
    if opcao == "3":
        if not tarefa:
            print("A lista está vazia")
        else:
            for x in range(len(tarefa)):
                print(f"- {tarefa[x]}: {x}")
            pergunta = int(input("Digite o número da tarefa que deseja deletar: "))
            tarefa.pop(pergunta)
            print("Tareda deleta com sucesso")

        """for x in range(len(tarefa)):
                        print(f"- {tarefa[x]}: {x}")
                        break
                tarefa.pop
                print("Tarefas deletadas com sucesso ")"""
