class cliente:
    def __init__(self, nome, cpf, tel):
        self.nome = nome
        self.nomeid=nome.upper()
        self.cpf = cpf
        self.situacao = 'OK'
        self.debito = 0
        self.tel = tel
        self.filmesAlugados = []


