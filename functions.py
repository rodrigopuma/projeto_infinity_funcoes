from time import sleep

def validador_resposta(choice, *args):
    while choice not in args:
        print(f'Escolha inválida. Opções válidas: {args}')
        choice = input('Selecione: ')
    return choice

def menu():
    print("""\033[1;31mMenu de Tarefas\033[m
    [0] - Criar Tarefa
    [1] - Ver todas Tarefas
    [2] - Marcar Tarefa como concluída
    [3] - Remover Tarefa
    [4] - Filtrar por prioridade
    [5] - Filtrar por categoria""")
    choice = input('Qual opção você deseja: ') 
    choice = validador_resposta(choice, '0', '1', '2', '3', '4', '5')
    return choice

def criar_tarefa():
    nome = input('\nDigite o nome: ')
    descricao = input('\nDigite a descrição: ')

    prioridade = input('\nDigite a prioridade: ')
    prioridade = validador_resposta(prioridade, 'alta', 'media', 'média', 'baixa')
    if 'média' == prioridade:
        prioridade = 'media'

    categoria = input('\nSelecione a categoria: ') # Quero fazer uma listinha de categorias
        
    tarefa = {
        'ID': None,
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
    renovar_ids(lista)

def renovar_ids(lista: list):
    contador = 0
    for tarefa in lista:
        contador += 1
        tarefa['ID'] = contador

def listar_tarefas(lista: list):
    renovar_ids(lista)
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
    renovar_ids(lista)
    index_prompt = solicitar_id('Qual tarefa você deseja concluir? (Pelo ID, se não quiser digite 0): ')
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

def exibir_tarefas_prioridade(lista: list):
    prioridade = input('Qual prioridade: ').lower()
    prioridade = validador_resposta(prioridade, 'alta', 'media', 'média', 'baixa')
    if 'média' == prioridade:
        prioridade = 'media'
    for tarefa in lista:
        if tarefa['prioridade'] == prioridade:
            print(f"""-----------------------
ID: {tarefa['ID']}
Nome: {tarefa['nome']}
Descrição: {tarefa['descrição']}
Categoria: {tarefa['categoria']}
Prioridade: {tarefa['prioridade']}
Status: {'Concluído' if tarefa['status concluido'] else 'Pendente'}
""")
        else:
            pass

def exibir_tarefas_categoria(lista: list, categoria: str):
    for tarefa in lista:
        if tarefa['categoria'] == categoria:
            print(f"""-----------------------
ID: {tarefa['ID']}
Nome: {tarefa['nome']}
Descrição: {tarefa['descrição']}
Categoria: {tarefa['categoria']}
Prioridade: {tarefa['prioridade']}
Status: {'Concluído' if tarefa['status concluido'] else 'Pendente'}
""")
        else:
            pass

def solicitar_id(mensagem: str):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Digite um número válido.')

def remover_tarefa(lista: list):
    renovar_ids(lista)
    index_prompt = solicitar_id('Qual tarefa você deseja excluir? (Pelo ID, se não quiser digite 0): ')
    if index_prompt != 0:
        for tarefa in lista:
            if tarefa['ID'] == index_prompt:
                lista.remove(tarefa)
                print('Tarefa removida com sucesso.')
                break
        else:
            print('ID não encontrado.')
    else:
        print('Ok! Voltando ao menu inicial.')

