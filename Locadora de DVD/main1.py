#!usr/bin/python
#_*_coding:utf-8_*_
# MAIN.PY --- Funcoes e Classes mais pertinentes em relacao ao programa
#    modulos para execucao em segundo plano
#

#___METAS_________-
#   - Implementar a conta do valor de acordo com Dia da Semana e Categoria
#   - Terminar metodo de "devolucao"

import shelve
from cliente import cliente
from produto import produto
from datetime import date
from carrinho import carrinho

class loja:

    #Ira procurar o cliente por CPF no banco de dados de Clientes
    def __procurarClienteCPF(self,cpfCliente = None):
        clientes = shelve.open("clientes.txt")
        if len(clientes) == 0:   #Retorna erro se o banco de dados estiver vazio
            return "Banco de dados vazio!!", False
        for keys in clientes:
            clienteEncontrado = clientes[keys]
            if clienteEncontrado.cpf == cpfCliente:
                clientes.close()
                print "%s foi encontrado"%(clienteEncontrado.nome)
                return clienteEncontrado
        clientes.close()
        return "Cliente não encontrado", False

    def __procurarFilme(self, nomeFilme=None,codigo=None):
        filmes = shelve.open("filmes.txt")
        if nomeFilme==None and codigo==None:
            filmes.close()
            return "Por favor, preencha os campos para pesquisa",False
        if nomeFilme==None or (nomeFilme!=None and codigo!=None):
            for x in filmes:
                if filmes[x].codigo == codigo:
                    filmeEncontrado=filmes[x]
                    return filmeEncontrado,filmes.close()
        if codigo==None:
           if filmes.has_key(nomeFilme)==True:
                filmeEncontrado = filmes[nomeFilme]
                return filmeEncontrado,filmes.close()
        else:
            filmes.close()
            return "Filme não encontrado", False


    #Procurar Cliente pelo NOME no banco de dados de Clientes
    def __procurarClienteNome(self,nomeCliente=None):
        clientes = shelve.open("clientes.txt")
        if len(clientes) == 0:
            return "Banco de dados vazio!!", False
        for keys in clientes:
            if keys == nomeCliente:
                clienteEncontrado = clientes[nomeCliente]
                clientes.close()
                print "%s foi encontrado"%(clienteEncontrado.nome)
                return clienteEncontrado
        clientes.close()
        return "Cliente não encontrado", False

    #Função Privada para cadastrar lotes de filmes
    def __cadastrarFilmes(self,nomeFilme=None,codigo=None,qtd=None,Midia=None):
        filmes = shelve.open("filmes.txt", writeback=True)
        if nomeFilme==None or codigo==None or qtd==None or Midia==None:
            filmes.close()
            return "Campos em branco", False
        if filmes.has_key(nomeFilme)==True and filmes[nomeFilme].codigo==codigo:
            filmes.close()
            return "Filme já cadastrado no Banco de Dados", False
        else:
            dataHj = date.today()
            f=produto(nomeFilme,codigo,qtd,dataHj,Midia)
            filmes[nomeFilme]=f
            filmes.close()
            return "Filme cadastrado com sucesso", True

    #Função Privada para cadastrar Clientes
    def __cadastrarClientes(self, nome = None, CPF = None):
        clientes = shelve.open("clientes.txt", writeback = True)
        if nome == None or CPF == None:
            clientes.close()
            return False
        if clientes.has_key(nome) == True and clientes[nome].cpf == CPF:
            return "Cliente já cadastrado.", False
        else:
            c = cliente(nome, CPF)
            clientes[nome] = c
            clientes.close()
            return "Cliente cadastrado com exito", True


    def procurarCliente(self,nomeCliente=None,cpf=None):
        if nomeCliente==None and cpf==None:
            return "Preencha um dos campos", False

        if nomeCliente==None or (nomeCliente!=None and cpf!=None):
            try:
                self.__procurarClienteCPF(cpf)
            except IOError:
                return False
        if cpf==None:
            try:
                self.__procurarClienteNome(nomeCliente)
            except IOError:
                return False


    def cadastroCliente(self, nome = None, cpf = None):
        try:
            self.__cadastrarClientes(nome, cpf)
        except IOError,False:
            return "Erro ao tentar cadastrar o Cliente", False

    def cadastroFilme(self, nome, codigo, quantidade, midia):
        try:
            self.__cadastrarFilmes(nome,codigo,quantidade,midia)
        except IOError, False:
            return "Erro ao tentar cadastrar o Filme no Database", False


    def alugar(self,filmes=None):
        if filmes==None:
           if len(carrinho.carrinhoDeCompras)!=0:
               filmes=carrinho.carrinhoDeCompras
               clientes = shelve.open("clientes.txt", writeback=True)
               dataHj = datetime.today()

           else:
                return "Carrinho de Compras Vazio![Erro 1]", False



