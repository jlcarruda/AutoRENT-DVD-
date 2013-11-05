class produto:
    def __init__(self,titulo, codigo, qtd, dataCadastro, midia):
        self.titulo = titulo
        self.categoria = 0
        self.codigo = codigo
        self.quantidade = qtd
        self.dataCadastro = dataCadastro
        '''O atributo dataCadastro vai ser definido
        na funcao de cadastroFilme, no main.py '''
        self.midia = midia
        self.reservas = 0
