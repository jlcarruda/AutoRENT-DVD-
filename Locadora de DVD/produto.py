from datetime import date
class produto:
    def __init__(self,titulo,codigo,qtd, midia,categoria):
        self.titulo=titulo
        self.midia = midia
        self.valor = 0
        self.dataAluguel = 0
        self.dataDevolucao = 0
        if self.midia.upper() == "DVD" or self.midia.upper() == "GAMES":
            self.midiavalor = 1
        else:
            self.midiavalor = 2
        self.codigo=codigo
        self.quantidade = qtd
        self.dataLancamento = "%s/%s/%s"%(str(date.today().day),str(date.today().month), str(date.today().year))
        self.categoria = categoria
        self.reservados = 0
        if self.categoria.upper() == "SUPER LANCAMENTO":
            self.estado=1.5
        if self.categoria.upper() == "LANCAMENTO":
            self.estado=1.25
        else:
            self.estado=1
        self.conta(self.estado, self.midiavalor) 

    def conta(self,estado,valormidia):
        diaSemana = ["Segunda", "Terca","Quarta","Quinta","Sexta","Sabado","Domingo"]
        today = diaSemana[date.today().weekday()]
        if today == 'Sabado' or today == 'Domingo':
            self.valor += (8.5)*valormidia*estado
        else:
            self.valor += (6.5)*valormidia*estado
        
