# Estrutura de dados

nome = ''
descricao = ''
prioridade = int()
categoria = ''
status = ''

def criar_tarefa():
    nome = input('\nDigite o nome: ')
    descricao = input('\nDigite a descrição: ')
    
    categoria = input('\nSelecione a categoria: ') # Quero fazer uma listinha de categorias
    status = input('\n[ Concluido | Fazer ]\nStatus: ')
    tarefa = {
        'Nome': nome,
        'Descrição Tarefa': descricao,
        'Categoria': categoria,
        'Status': status
    }
    return tarefa

def adicionar_tarefa_a_lista(tarefa, lista):
    lista.append(tarefa)
    salvar_tarefa(tarefa)

def listar_tarefas(lista_tarefas):
    lista_tarefas = []
    with open("lista_tarefas.txt", "r") as arquivo: # "r" = read (ler os usuarios)
        for tarefa in arquivo:
            tarefa.strip().split(';')
            
 
    for tarefa in lista_tarefas:
        contador += 1
        print(f'Tarefa {contador}:\n{tarefa}')

def salvar_tarefa(tarefa):
    with open("lista_tarefas.txt", "a") as arquivo: # "a" = append (adicionar ao final)
        arquivo.write(tarefa)
    
def marcar_tarefa_concluida(lista_tarefas, tarefa):
    for trf in lista_tarefas:
        if trf['Nome'] == tarefa['Nome']:
            tarefa['Status'] = 'Concluido'
            break
    return tarefa
