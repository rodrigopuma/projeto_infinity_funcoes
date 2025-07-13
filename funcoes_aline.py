tarefas = []

def add_tarefa():
    nome = input('Digite o nome da tarefa: ')
    descricao = input('Digite a descrição da tarefa: ')
    categoria = input('Digite a categoria: ')
    prioridade = input('Digite a prioridade: ')

    tarefa = {
        'nome': nome,
        'descricao': descricao,
        'categoria': categoria.lower(),
        'prioridade': prioridade.lower(),
        'concluido': False
    }

    tarefas.append(tarefa)

def marcar_como_concluido():
    pass