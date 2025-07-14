from functions import menu, criar_tarefa, adicionar_tarefa_lista, listar_tarefas, marcar_tarefa_concluida, remover_tarefa

# Estrutura de dados

lista_tarefas = []

while True:
    choice = menu()

    if choice == '0':
        adicionar_tarefa_lista(criar_tarefa(), lista_tarefas)

    if choice == '1':
        listar_tarefas(lista_tarefas)

    if choice == '2':
        listar_tarefas(lista_tarefas)
        marcar_tarefa_concluida(lista_tarefas)

    if choice == '3':
        listar_tarefas(lista_tarefas)
        remover_tarefa(lista_tarefas)
