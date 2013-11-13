#!usr/bin/python
#_*_coding:utf-8_*_
# MAIN.PY --- Funcoes e Classes mais pertinentes em relacao ao programa
#    modulos para execucao em segundo plano
#

#___METAS_________-
#   - Implementar a conta do valor de acordo com Dia da Semana e Categoria
#   - Terminar metodo de "devolucao"

import wx
import shelve
from cliente import cliente
from produto import produto
from datetime import date
from carrinho import carrinho

class loja:
    listaDeFilmes=[]
    lista=[]
    # -------------------------------------- FUNCOES PRIVADAS --------------------------------------
    #Ira procurar o cliente por CPF no banco de dados de Clientes
    def __procurarClienteCPF(self,cpfCliente = None):
        clientes = shelve.open("clientes")
        if cpfCliente==None:
            clientes.close()
            wx.MessageBox('Erro no Codigo', 'Erro', wx.OK|wx.ICON_ERROR)
        if len(clientes) == 0:   #Retorna erro se o banco de dados estiver vazio
            wx.MessageBox("Banco de dados vazio!!","Erro",wx.OK|wx.ICON_ERROR)
        for keys in clientes:
            clienteEncontrado = clientes[keys]
            if clienteEncontrado.cpf == cpfCliente:
                clientes.close()
                return clienteEncontrado, True
        clientes.close()
        return False

    #Procurar Cliente pelo NOME no banco de dados de Clientes
    def __procurarClienteNome(self,nomeCliente=None):
        clientes = shelve.open("clientes")
        if len(clientes) == 0:
            wx.MessageBox("Banco de Dados vazio!","Info",wx.OK|wx.ICON_INFORMATION)
        for keys in clientes:
            if keys == nomeCliente:
                clienteEncontrado = clientes[nomeCliente]
                clientes.close()
                print "%s foi encontrado"%(clienteEncontrado.nome)
                return clienteEncontrado
        clientes.close()
        wx.MessageBox("Cliente não encontrado","Info",wx.OK|wx.ICON_INFORMATION)
        return False

    #Função Privada para cadastrar lotes de filmes
    def __cadastrarFilmes(self,nomeFilme=None,codigo=None,qtd=None,Midia=None):
        filmes = shelve.open("filmes", writeback=True)
        if filmes.has_key(nomeFilme)==True and filmes[nomeFilme].codigo==codigo:
            filmes.close()
            wx.MessageBox("Filme já cadastrado no Banco de Dados",'Info',wx.OK|wx.ICON_INFORMATION)
            return False
        else:
            dataHj = date.today()
            f=produto(nomeFilme,codigo,qtd,dataHj,Midia)
            filmes[nomeFilme]=f
            filmes.close()
            wx.MessageBox("Filme cadastrado com sucesso",'Info',wx.OK|wx.ICON_INFORMATION)
            return True

    #Função Privada para cadastrar Clientes
    def __cadastrarClientes(self, nome = None, CPF = None):
        clientes = shelve.open("clientes", writeback = True)
        if nome == None or CPF == None:
            clientes.close()
            return False
        if clientes.has_key(nome) == True and clientes[nome].cpf == CPF:
            wx.MessageBos('Cliente ja cadastrado','Info',wx.OK|wx.ICON_INFORMATION)
            return False
        else:
            c = cliente(nome, CPF)
            clientes[nome] = c
            clientes.close()
            return "Cliente cadastrado com exito", True
    
    # Funcao que vai retornar uma lista de 10 congruencias 
    def __procurarFilme(self,titulo, codigo, categoria, midia):
        filmes=shelve.open("filmes")
        listaDeFilmes=[]
        if len(filmes)==0:
            wx.MessageBox('Banco de Dados Vazio!','Info',wx.OK|wx.ICON_INFORMATION)
            return False
        if (titulo == codigo) and (categoria==codigo) and (midia == categoria) and titulo=='': 
            for filme in filmes:
                if len(self.listaDeFilmes) == 10:
                    break
                self.listaDeFilmes.append(filmes[filme])
            return self.listaDeFilmes,filmes.close(),True
        
        if titulo=='' or (titulo!='' and codigo!=''):
            for x in filmes:
                if len(self.listaDeFilmes) == 10:
                    break
                if filmes[x].codigo == codigo:
                    filmeEncontrado=filmes[x]
                    self.listaDeFilmes.append(filmeEncontrado)
            return self.listaDeFilmes,filmes.close(), True   

        if titulo!='':
            if filmes.has_key(titulo)==True:
                filmeEncontrado = filmes[nomeFilme]
                self.listaDeFilmes.append(filmeEncontrado)
                filmes.close()
                return self.listaDeFilmes, True
            else:
                return False
            
        if midia!='':
            for filme in filmes:
                if len(self.listaDeFilmes) == 10:
                    break
                if filmes[filme].midia == midia:
                    self.listaDeFilmes.append(filmes[filme])
            return self.listaDeFilmes, filmes.close(), True

        if categoria!='':
            for filme in filmes:
                if len(self.listaDeFilmes)==10:
                    break
                if filmes[filme].categoria == categoria:
                    self.listaDeFilmes.append(filmes[filme])
            return self.listaDeFilmes, filmes.close(), True

        else:
            filmes.close()
            wx.MessageBox('Filme nao Encontrado','Info', wx.OK|wx.ICON_INFORMATION)


    # -------------------------------- FUNÇOES EFETIVAS ---------------------------------------------------
    def procurarCliente(self,nomeCliente=None,cpf=None):
        if nomeCliente==None and cpf==None:
            return "Preencha um dos campos", False

        if nomeCliente==None or (nomeCliente!=None and cpf!=None):
            try:
                self.__procurarClienteCPF(cpf)
            except:
                wx.MessageBox("Cliente não encontrado","Info",wx.OK|wx.ICON_INFORMATION)
        if cpf==None:
            try:
                self.__procurarClienteNome(nomeCliente)
            except:
                wx.MessageBox("Cliente não encontrado","Info",wx.OK|wx.ICON_INFORMATION)
                
    
    def cadastroCliente(self, nome = None, cpf = None):
        try:
            self.__cadastrarClientes(nome, cpf)
        except:
            return "Erro ao tentar cadastrar o Cliente", False

    def cadastroFilme(self, nome, codigo, quantidade, midia):
        try:
            self.__cadastrarFilmes(nome,codigo,quantidade,midia)
        except:
            return False

    def procurarFilme(self,titulo,codigo, categoria,midia): 
        try:
            self.lista = self.__procurarFilme(titulo,codigo,categoria,midia)
            return self.lista[0]
        except:
            wx.MessageBox('Erro ao procurar Filme','Error',wx.OK|wx.ICON_INFORMATION)
            return False
            
    def alugar(self,filmes=None):
        if filmes==None:
           if len(carrinho.carrinhoDeCompras)!=0:
               filmes=carrinho.carrinhoDeCompras
               clientes = shelve.open("clientes.txt", writeback=True)
               dataHj = datetime.today()

           else:
                return "Carrinho de Compras Vazio![Erro 1]", False



