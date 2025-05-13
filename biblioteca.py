"""def listaTarefas(lista):
    continuar = input("Deseja adicionar uma tarefa hoje? (s/n): ")

    for i in range(len(lista)):
        if continuar == "s":
            lista[i] = input("Digite sua tarefa: ")
            continuar = input("Deseja adicionar mais tarefa? (s/n):  ")
        else:
            break
            print("-") * 60
    print()
    if lista != " ":
        print("Suas tarefas do dia são: ")
        for x in lista:
            print("-", x)"""

lista = [1,2,3]
for i in range(len(lista)):

    print(len(i))