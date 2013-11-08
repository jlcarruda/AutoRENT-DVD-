class carrinho:
    carrinhoDeCompras ={}
    def add(self, filme):
        self.carrinhoDeCompras[filme.titulo] = filme
    def remove(self,filme):
        if carrinhoDeCompras.has_key(filme.titulo):
            del carrinhoDeCompras[filme.titulo]
        else:
            return False
    def alugar(self):
        if len(self.carrinhoDeCompras)==0:
            return "Carrinho de compras Vazio"
