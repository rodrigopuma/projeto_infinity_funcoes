from time import sleep

def validador_resposta(choice, *args):
    if choice in args:
        pass
    else:
        print(f'Escolha inválida selecione uma opção válida\n'
              f'Opções: {args}')
        choice = input('Selecione: ')
    return choice

def menu():
    print("""\033[1;31mMenu de Tarefas\033[m
    [0] - Criar Tarefa
    [1] - Ver todas Tarefas
    [2] - Marcar Tarefa como concluída
    [3] - Remover Tarefa""")
    choice = input('Qual opção você deseja: ') 
    choice = validador_resposta(choice, '0', '1', '2', '3')
    return choice

def criar_tarefa():
    nome = input('\nDigite o nome: ')
    descricao = input('\nDigite a descrição: ')
    prioridade = input('\nDigite a prioridade: ')
    categoria = input('\nSelecione a categoria: ') # Quero fazer uma listinha de categorias
        
    tarefa = {
        'ID': int,
        'nome': nome,
        'descrição': descricao,
        'categoria': categoria.lower(),
        'prioridade': prioridade.lower(),
        'status concluido': False
    }

    return tarefa

def adicionar_tarefa_lista(tarefa: dict, lista: list):
    lista.append(tarefa)
    print('Tarefa adicionada com sucesso!')
    tarefa['ID'] = adicionar_id(tarefa, lista)

def adicionar_id(tarefa: None, lista: list):
    contador = 0
    for tarefa in lista:
        contador += 1
        tarefa['ID'] = contador
    return tarefa['ID']

def listar_tarefas(lista: list):
    for tarefa in lista:
        sleep(0.3)
        print(f"""-----------------------
ID: {tarefa['ID']}
Nome: {tarefa['nome']}
Descrição: {tarefa['descrição']}
Categoria: {tarefa['categoria']}
Prioridade: {tarefa['prioridade']}
Status: {'Concluído' if tarefa['status concluido'] is True else 'Pendente'}
""")

def marcar_tarefa_concluida(lista: list):
    index_prompt = int(input('Qual tarefa você deseja concluir? (Pelo ID, se não quiser digite 0): '))
    if index_prompt != 0:
        for tarefa in lista:
            if tarefa['ID'] == index_prompt:
                tarefa['status concluido'] = True
                break
            else: pass
        else:
            print('Não foi encontrado nenhum ID para essa tarefa.')
    else:
        print('Ok! Voltando ao menu inicial.')

def remover_tarefa(lista: list):
    index_prompt = int(input('Qual tarefa você deseja excluir? (Pelo ID, se não quiser digite 0): '))
    if index_prompt != 0:
        index_prompt -= 1 # Para se alinhar ao indice da lista de tarefas
        lista.pop(index_prompt)
    else:
        print('Ok! Voltando ao menu inicial.')
