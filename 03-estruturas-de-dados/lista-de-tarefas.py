def adicionar_tarefa(tarefas):
    nova_tarefa = input("\nNome da tarefa: ")
    tarefas.append({"nome": nova_tarefa, "status": False})

def listar_tarefas(tarefas):
    if len(tarefas) > 0:
        print()
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i} - {'[X]' if tarefa['status'] else '[ ]'} {tarefa['nome']}")
    else:
        print("\nNão há nenhuma tarefa cadastrada.")

def atualizar_status(tarefas):
    if len(tarefas) > 0:
        num_tarefa = int(input("\nInforme o número da tarefa: "))

        try:
            tarefas[num_tarefa - 1]["status"] = True
        except(IndexError, ValueError):
            print("\nEssa tarefa não existe.")
    else:
        print("\nNão há nenhuma tarefa cadastrada.")

tarefas = []

while True:
    print("\n-=-=-=- MENU: LISTA DE TAREFAS -=-=-=-\n"
        "1- Adicionar tarefa\n"
        "2- Listar tarefas\n"
        "3- Marcar como feita\n"
        "4- Sair")

    opcao = input("Opção: ")

    match opcao:
        case "1":
            adicionar_tarefa(tarefas)
        case "2":
            listar_tarefas(tarefas)
        case "3":
            atualizar_status(tarefas)
        case "4":
            break
        case _:
            print("\nOpção inválida.")