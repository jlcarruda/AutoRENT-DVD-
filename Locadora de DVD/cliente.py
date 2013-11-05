class cliente:
    def __init__(self, nome, cpf):
        self.nome = nome.upper()
        self.cpf = cpf
        self.situacao = True
        self.debito = 0
        self.filmesAlugados = {}


