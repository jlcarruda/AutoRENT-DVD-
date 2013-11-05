class carrinho:
    carrinhoDeCompras ={}
    def add(self, filme):
        self.carrinhoDeCompras[filme.nome] = filme
    def remove(self,filme):
        if carrinhoDeCompras.has_key(filme.nome):
            del carrinhoDeCompras[filme.nome]
        else:
            return False
    def alugar(self):
        if len(self.carrinhoDeCompras)==0:
            return "Carrinho de compras Vazio"
