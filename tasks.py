import json
import os

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("\nNenhuma tarefa cadastrada.\n")
        return

    print("\nLISTA DE TAREFAS:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. [{task['status']}] {task['descricao']}")
    print()

def add_task():
    description = input("\nDigite o nome da nova atividade: ")
    new = {"descricao": description, "status": "pendente"}

    tasks = load_tasks()
    tasks.append(new)
    save_tasks(tasks)

    print("Tarefa cadastrada!\n")

def set_on_progress():
    tasks = load_tasks()
    show_tasks()
    try:
        num = int(input("Selecione o número da tarefa a colocar em andamento: ")) - 1
        tasks[num]["status"] = "em andamento"
        save_tasks(tasks)
        print("Tarefa agora está em andamento!\n")
    except:
        print("Opção inválida.\n")

def close_task():
    tasks = load_tasks()
    show_tasks()
    try:
        num = int(input("Selecione a tarefa que deseja finalizar: ")) - 1
        tasks[num]["status"] = "finalizada"
        save_tasks(tasks)
        print("Tarefa finalizada!\n")
    except:
        print("Opção inválida.\n")

def edit_task():
    tasks = load_tasks()
    show_tasks()
    try:
        num = int(input("Selecione a tarefa para editar: ")) - 1
        new_desc = input("Digite a nova descrição: ")
        tasks[num]["descricao"] = new_desc
        save_tasks(tasks)
        print("Tarefa editada!\n")
    except:
        print("Opção inválida.\n")

def remove_task():
    tasks = load_tasks()
    show_tasks()
    try:
        num = int(input("Selecione a tarefa para remover: ")) - 1
        tasks.pop(num)
        save_tasks(tasks)
        print("Tarefa removida!\n")
    except:
        print("Opção inválida.\n")

def menu():
    while True:
        print("===== MEU TO DO LIST =====")
        print("1 - Mostrar tarefas")
        print("2 - Cadastrar nova atividade")
        print("3 - Colocar tarefa em andamento")
        print("4 - Finalizar tarefa")
        print("5 - Editar atividade")
        print("6 - Excluir atividade")
        print("0 - Sair")
        
        option = input("\nEscolha uma opção: ")

        if option == "1":
            show_tasks()
        elif option == "2":
            add_task()
        elif option == "3":
            set_on_progress()
        elif option == "4":
            close_task()
        elif option == "5":
            edit_task()
        elif option == "6":
            remove_task()
        elif option == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

menu()
