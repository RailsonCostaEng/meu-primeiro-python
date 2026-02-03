lista_de_tarefas =[]
print("---Meu gerenciador de tarefas---")
while True:
    tarefa = input("digite uma tarefa(ou 'sair'): ")
    if tarefa == "sair":
        break
    lista_de_tarefas.append(tarefa)
    print(f"Sua lista agora: {lista_de_tarefas} ")
    print("--- Suas tarefas ---")
    for item in lista_de_tarefas:
        print(f"- {item}")