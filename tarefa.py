
class Tarefa:
    def __init__(self, titulo, descricao, categoria, concluida=False):
        self.titulo = titulo
        self.descricao = descricao
        self.categoria = categoria
        self.concluida = concluida

    def concluir(self):
        self.concluida = True
        
    def to_dict(self):
        return { "titulo" : self.titulo,
                "descricao" : self.descricao, 
                "categoria" : self.categoria,
                "concluida" : self.concluida 
                }
        
    @classmethod
    def from_dict(cls, data):
        tarefa = cls (
            data['titulo'],
            data['descricao'],
            data['categoria']
        )
        tarefa.concluida = data['concluida']
        return tarefa
    
    
    def __repr__(self):
        status = 'Concluída' if self.concluida else 'Pendente'
        return f'\nTítulo: {self.titulo} \nDescrição: {self.descricao}\nCategoria: {self.categoria}\nStatus: {status}'

