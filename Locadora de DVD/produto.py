class produto:
    def __init__(self,titulo, codigo, qtd, dataCadastro, midia):
        self.titulo = titulo
        self.categoria = 'Super Lancamento'
        self.codigo = codigo
        self.quantidade = qtd
        self.dataCadastro = dataCadastro
        '''O atributo dataCadastro vai ser definido
        na funcao de cadastroFilme, no main1.py '''
        self.midia = midia
        self.reservas = 0
