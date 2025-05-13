lista = [" "]*5
adicionar = " "
apagar = " "
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
print()
adicionar = input("Deseja adicionar uma nova tarefa na lista? (s/n): ")

while adicionar == "s" or adicionar == "S":
    tarefaNova = input("Digite sua tarefa: ")
    lista.append(tarefaNova)
    for x in lista:
        if x != " ":
            print("Suas tarefas do dia são: ")
            print("-", x)
    adicionar = input("Deseja adicionar uma nova tarefa na lista? (s/n): ")
    print()
else:
    apagar = input("Deseja excluir algumas tarefa? (s/n): ")
    if apagar == "s" or apagar == "S":
        for x in lista:
            if x != " ":
                print(f"- {x} \n"
                      f"número da tarefa {cont}")
        print("-" * 60)

