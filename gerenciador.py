from tarefa import Tarefa
import json

ARQUIVO_TAREFAS = "tarefas.json"

class GerenciadorDeTarefas:

    def __init__(self):
        self.lista_de_tarefas = []
        self.carregar()

    def adicionar_tarefa(self, titulo, descricao, categoria):
        tarefa = Tarefa(titulo, descricao, categoria)
        self.lista_de_tarefas.append(tarefa)
        self.salvar()
    
    def listar_tarefas(self):
        return self.lista_de_tarefas
    
    def concluir_tarefa(self, titulo):
        for tarefa in self.lista_de_tarefas:
            if tarefa.titulo == titulo:
                tarefa.concluir()
                self.salvar()
                return True
        return False
            
    def remover_tarefa(self, titulo):
        for tarefa in self.lista_de_tarefas:
            if tarefa.titulo == titulo:
                self.lista_de_tarefas.remove(tarefa)
                self.salvar()
                return True
        return False

    def filtrar_por_categoria(self, categoria):
        tarefas_filtradas = []
        for lista_de_tarefas in self.lista_de_tarefas:
            if lista_de_tarefas.categoria == categoria:
                tarefas_filtradas.append(lista_de_tarefas)
        return tarefas_filtradas

    
    def estatisticas(self):
        total = len(self.lista_de_tarefas)

        concluidas = 0
        for tarefa in self.lista_de_tarefas:
            if tarefa.concluida:
                concluidas += 1
                        
        pendentes = total - concluidas
        
        return {
            'total': total,
            'concluidas': concluidas,
            'pendentes': pendentes
        }

    def salvar(self):
        dados = [t.to_dict() for t in self.lista_de_tarefas] 
        with open(ARQUIVO_TAREFAS, 'w', encoding='utf8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            
    def carregar(self):
        try:
            with open(ARQUIVO_TAREFAS, 'r', encoding='utf8') as arquivo:
                dados = json.load(arquivo)

            self.lista_de_tarefas = [
                    Tarefa.from_dict(d) for d in dados
            ]
                    
        except FileNotFoundError:
            self.lista_de_tarefas = []
            
    

    


