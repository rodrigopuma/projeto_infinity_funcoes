# Estrutura de dados

def criar_tarefa():
    nome = input('\nDigite o nome: ')
    descricao = input('\nDigite a descrição: ')
    prioridade = input('\nDigite a prioridade: ')
    categoria = input('\nSelecione a categoria: ') # Quero fazer uma listinha de categorias
    concluido = False
    tarefa = {
        'Nome': nome,
        'Descrição Tarefa': descricao,
        'Categoria': categoria,
        'Prioridade': prioridade,
        'Status Concluido': concluido 
    }
    return tarefa

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
