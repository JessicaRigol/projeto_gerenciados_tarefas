from gerenciador import GerenciadorDeTarefas 
import os

ger = GerenciadorDeTarefas()
#os.system('cls')

while True:
    print('===== GERENCIADOR DE TAREFAS =====')
    print('1 - Adicionar tarefa\n'
        '2 - Listar tarefas\n'
        '3 - Concluir tarefa\n'
        '4 - Remover tarefa\n'
        '5 - Filtrar por categoria\n'
        '6 - Estatísticas\n'
        '0 - Sair\n')
    
    try:
        op = int(input('Escolha o número da opção desejada: '))

        if op == 1:
            titulo = input('Título da tarefa: ')
            descricao = input('Descrição da tarefa: ')
            categoria = input('Categoria da tarefa: ')
            ger.adicionar_tarefa(titulo, descricao, categoria)
        
        elif op == 2:
            tarefas = ger.listar_tarefas()
            print('TAREFAS:')
            for tarefa in tarefas:
                print(tarefa)
                print()
        
        elif op == 3:
            titulo = input('Digite o título da tarefa concluida: ')
            if ger.concluir_tarefa(titulo):
                print('Tarefa concluída!')
                print()
            else:
                print('Tarefa não existe.')
        
        elif op == 4:
            titulo = input('Digite o título da tarefa que deseja remover: ')
            if ger.remover_tarefa(titulo):
                print('Tarefa removida!')
                print()
            else:
                print('Tarefa não encontrada.')
        
        elif op == 5:
            categoria = input('Digite a categoria da tarefa: ')
            print(f'Tarefas da categoria {categoria}:')
            
            categorias_filtradas = ger.filtrar_por_categoria(categoria)
            
            if categorias_filtradas:
                for tarefas in categorias_filtradas:
                    print(tarefas)
                    print()
            else:
                print('Categoria não encontrada.')
        
        elif op == 6:
            stats = ger.estatisticas()
            print(f"Total de tarefas: {stats['total']}")
            print(f"Concluídas: {stats['concluidas']}")
            print(f"Pendentes: {stats['pendentes']}")
            print()
        
        elif op == 0:
            print('Desligado')
            break

    except ValueError:
        print('Opção inválida! Escolha o número da opção desejada:')


    