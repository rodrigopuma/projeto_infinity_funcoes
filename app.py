from functions import menu, criar_tarefa, adicionar_tarefa_lista, listar_tarefas, marcar_tarefa_concluida

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

    


# def adicionar_tarefa_a_lista(tarefa):
#     salvar_tarefa(tarefa)

# def listar_tarefas():
#     contador = 0
#     with open("lista_tarefas.txt", "r") as arquivo: # "r" = read (ler os usuarios)
#         for tarefa in arquivo:
#             tarefa.strip().split(',')
#             contador += 1
#             print(f'Tarefa {contador}:\n{tarefa}')

# def salvar_tarefa(tarefa):
#     with open("lista_tarefas.txt", "a") as arquivo: # "a" = append (adicionar ao final)
#         arquivo.write(str(tarefa))
    
# def marcar_tarefa_concluida(lista_tarefas, tarefa):
#     for trf in lista_tarefas:
#         if trf['Nome'] == tarefa['Nome']:
#             tarefa['Status'] = 'Concluido'
#             break
#     return tarefa

# tarefa = criar_tarefa()
# adicionar_tarefa_a_lista(tarefa)
# listar_tarefas()
