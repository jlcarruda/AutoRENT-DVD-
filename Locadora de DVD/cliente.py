class cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.nomeid=nome.upper()
        self.cpf = cpf
        self.situacao = 'OK'
        self.debito = 0
        self.filmesAlugados = {}


