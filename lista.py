lista = [" "]
continuar = input("Deseja adicionar uma tarefa hoje? (s/n): ")
print("-" * 60)

for i in range(len(lista)):
    if continuar == "s":
        lista[i] = input("Digite sua tarefa: ")
        continuar = input("Deseja adicionar mais tarefa? (s/n):  ")
        print("-"*60)

    else:
        break
        print("-"*60)
print()
for x in lista:
    if x != " ":
        print("Suas tarefas do dia são: ")
        print("-",x)