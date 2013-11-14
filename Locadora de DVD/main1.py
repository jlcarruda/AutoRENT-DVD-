#!usr/bin/python
#_*_coding:utf-8_*_
# MAIN.PY --- Funcoes e Classes mais pertinentes em relacao ao programa
#    modulos para execucao em segundo plano
#

#___METAS_________-
#   - Implementar a conta do valor de acordo com Dia da Semana e Categoria
#   - Implementar o metodo de "Alugar" e "Devolver"
#   - Consertar Procura de Clientes por CPF/Nome (Publica e Privada)
#   - Implementar os metodos de "Remover Cliente" e "Remover Filmes"

import wx
import shelve
from cliente import cliente
from produto import produto
from datetime import date

class loja:
    listaDeFilmes=[]
    lista=[]
    listaDeClientes=[]
    # -------------------------------------- FUNCOES PRIVADAS --------------------------------------
    def __removerCliente(self,nome, cpf):
        if nome =='' or cpf == '':
            wx.MessageBox("Nome e/ou CPF nao especificados","Error",wx.OK|wx.ICON_ERROR)
            return False
        clientes = shelve.open("clientes")
        if clientes.has_key(nome.upper()):
            if clientes[nome.upper()].cpf == cpf:
                if clientes[nome.upper()].situacao == "OK":
                    del clientes[nome.upper()]
                    clientes.close()
                    wx.MessageBox("Cliente removido.","Info",wx.OK|wx.ICON_INFORMATION)
                else:
                    clientes.close()
                    return "Cliente em debito", False
            else:
                return "CPF especificado nao permitido",False
        else:
            clientes.close()
            return "Cliente nao encontrado!", False
            
    def __procurarClienteAll(self,nomeCliente,cpfCliente):
        clientes=shelve.open('clientes')
        if clientes.has_key(nomeCliente.upper()):
            if clientes[nomeCliente.upper()].cpf == cpfCliente:
                self.listaDeClientes.append(clientes[nomeCliente.upper()])
                clientes.close()
                return self.listaDeClientes 
        if clientes.has_key(nomeCliente.upper())==False:
            for x in clientes:
                if x[:len(nomeCliente)] == nomeCliente.upper():
                    if clientes[x].cpf==cpfCliente:
                        self.listaDeClientes.append(clientes[x])
                        clientes.close()
                        return self.listaDeClientes
        elif len(listaDeClientes)==0:
            wx.MessageBox('Cliente nao Encontrado','Info',wx.OK|wx.ICON_INFORMATION)
            clientes.close()
            return self.listaDeClientes
        
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
                self.listaDeClientes.append(clienteEncontrado)
                return self.listaDeClientes
            elif clientes[keys].cpf[:len(cpfCliente)] == cpfCliente:
                self.listaDeClientes.append(clienteEncontrado)
        clientes.close()
        if len(self.listaDeClientes)==0:
            wx.MessageBox('Nenhum Cliente Encontrado','Erro')
        return self.listaDeClientes

    #Procurar Cliente pelo NOME no banco de dados de Clientes
    def __procurarClienteNome(self,nomeCliente):
        clientes = shelve.open("clientes")
        if len(clientes) == 0:
            wx.MessageBox("Banco de Dados vazio!","Info",wx.OK|wx.ICON_INFORMATION)
        if nomeCliente!='':
            if clientes.has_key(nomeCliente):
                clienteEncontrado = clientes[nomeCliente]
                clientes.close()
                self.listaDeClientes.append(clienteEncontrado)
                return self.listaDeClientes
            else:
                for keys in clientes:
                    if keys[:len(nomeCliente)].upper() == nomeCliente.upper():
                        self.listaDeClientes.append(clientes[keys])
                clientes.close()
                return self.listaDeClientes        
        else:
            for keys in clientes:
                self.listaDeClientes.append(clientes[keys])
                
        clientes.close()
        return self.listaDeClientes
        wx.MessageBox('Varias Congruencias')
                

    #Função Privada para cadastrar lotes de filmes
    def __cadastrarFilmes(self,nomeFilme=None,codigo=None,qtd=None,Midia=None,categoria=None):
        filmes = shelve.open("filmes", writeback=True)
        if filmes.has_key(nomeFilme)==True and filmes[nomeFilme].codigo==codigo:
            filmes.close()
            wx.MessageBox("Filme já cadastrado no Banco de Dados",'Info',wx.OK|wx.ICON_INFORMATION)
            return False
        else:
            try:
                f=produto(nomeFilme,codigo,qtd,Midia,categoria)
            except:
                wx.MessageBox('Erro ao instanciar o Produto')
            filmes[f.titulo]=f
            filmes.close()      
            

    #Função Privada para cadastrar Clientes
    def __cadastrarClientes(self, nome = None, CPF = None, Tel=None):
        clientes = shelve.open("clientes", writeback = True)
        if nome == None or CPF == None or Tel==None:
            clientes.close()
            return False
        if clientes.has_key(nome) == True and clientes[nome].cpf == CPF:
            wx.MessageBos('Cliente ja cadastrado','Info',wx.OK|wx.ICON_INFORMATION)
            return False
        else:
            c = cliente(nome, CPF, Tel)
            clientes[c.nomeid] = c
            clientes.close()
            return "Cliente cadastrado com exito", True
    
    # Funcao que vai retornar uma lista de 10 congruencias 
    def __procurarFilme(self,titulo, codigo, categoria, midia):
        filmes=shelve.open("filmes")
        listaDeFilmes=[]
        if len(filmes)==0:
            wx.MessageBox('Banco de Dados Vazio!','Info',wx.OK|wx.ICON_INFORMATION)
        if (titulo == codigo) and (categoria==titulo) and (midia == titulo) and titulo=='': 
            for filme in filmes:
                self.listaDeFilmes.append(filmes[filme])
            filmes.close()
            return self.listaDeFilmes
        
        if titulo=='' or (titulo!='' and codigo!=''):
            for x in filmes:
                if filmes[x].codigo == codigo:
                    filmeEncontrado=filmes[x]
                    self.listaDeFilmes.append(filmeEncontrado)
            filmes.close()
            return self.listaDeFilmes  

        if titulo!='':
            if filmes.has_key(titulo):
                filmeEncontrado = filmes[nomeFilme]
                self.listaDeFilmes.append(filmeEncontrado)
                filmes.close()
                return self.listaDeFilmes
            else:
                for filme in filmes:
                    if filme[:len(titulo)].upper()==titulo.upper():
                        self.listaDeFilmes.append(filmes[filme])
                if len(self.listaDeFilmes)==0:                
                    filmes.close()
            
        if midia!='':
            for filme in filmes:
                if len(self.listaDeFilmes) == 10:
                    break
                if filmes[filme].midia == midia:
                    self.listaDeFilmes.append(filmes[filme])
            filmes.close()
            return self.listaDeFilmes

        if categoria!='':
            for filme in filmes:
                if len(self.listaDeFilmes)==10:
                    break
                if filmes[filme].categoria == categoria:
                    self.listaDeFilmes.append(filmes[filme])
            filmes.close()
            return self.listaDeFilmes
        

        else:
            filmes.close()
            return self.listaDeFilmes

    # -------------------------------- FUNÇOES EFETIVAS ---------------------------------------------------
    def procurarCliente(self,nomeCliente,cpf):
        self.lista=[]
        self.listaDeClientes=[]
        if nomeCliente!='' and cpf!='':
            try:
                self.lista=self.__procurarClienteAll(nomeCliente,cpf)
                return self.lista
            except:
                wx.MessageBox('Erro Aqui')
        if (nomeCliente=='' and cpf=='') or cpf=='' or nomeCliente!='':
            try:
                self.lista=self.__procurarClienteNome(nomeCliente)
                return self.lista
            except:
                wx.MessageBox('Error ao procurar Cliente por Nome','Error',wx.OK|wx.ICON_INFORMATION)
        elif nomeCliente=='':
            try:
                self.lista = self.__procurarClienteCPF(cpf)
                return self.lista
            except:
                wx.MessageBox('Error ao procurar Cliente por CPF',"Error",wx.OK|wx.ICON_ERROR)
            
            
    def cadastroCliente(self, nome = None, cpf = None, Tel=None):
        try:
            self.__cadastrarClientes(nome, cpf, Tel)
        except:
            return "Erro ao tentar cadastrar o Cliente", False

    def cadastroFilme(self, nome, codigo, quantidade, midia,categoria):
        try:
            self.__cadastrarFilmes(nome,codigo,quantidade,midia,categoria)
        except:
            return False

    def procurarFilme(self,titulo,codigo, categoria,midia): 
        if len(self.listaDeFilmes)>0:
           self.listaDeFilmes=[]
        if len(self.lista)>0:
            self.lista=[]
        try:
            self.lista = self.__procurarFilme(titulo,codigo,categoria,midia)
            return self.lista
        except:
            wx.MessageBox('Erro ao procurar Filme','Error',wx.OK|wx.ICON_INFORMATION)
            return False

    def removerCliente(self,nomeCliente,cpf):
        try:
            self.__removerCliente(nomeCliente,cpf)
        except:
            wx.MessageBox('Erro ao remover o Cliente','Error',wx.OK|wx.ICON_ERROR)
            


    def reserva(CarrinhodeCompras = None, nomeCliente = None, cpfCliente = None, diasparaalugar = None):
        if CarrinhodeCompras == None:
            return "Erro! Produtos não especificados",False
        if len(CarrinhodeCompras) == 0:
            return "Erro! Nenhum produto selecionado",False
        if len(CarrinhodeCompras) > 4:
            return "Erro! Só podem ser reservados ate quatro filmes",False
        #Verifica se o usuario preencheu a forma de pagamento
        filmes = shelve.open("filmes")
        clientes = shelve.open("clientes") #Clientes eh o ARQUIVO

        for c in clientes:
            if clientes[c].nome == nomeCliente:
                if cpfCliente != None and clientes[c].cpf == cpfCliente:
                    c = clientes[c]
                    break
                else:
                    return "Erro! CPF nao especificado ou congruencia entre CPF/Nome nao encontrada.", False

        valor = conta(CarrinhodeCompras = None)
        if len(CarrinhodeCompras)>0:
            today = date.today()
            dataAluguel = date.fromordinal(date.toordinal(today)+diasparaalugar) #Data na qual o DVD esta sendo alugado
            diaAluguel = dataDevolucao.weekday()

            if diaAluguel == 6:
                dataAluguel = date.fromordinal(date.toordinal(dataDevolucao)+1)
                
            for nomefilme in CarrinhodeCompras:
                if filmes[nomeFilme].qtd != 0:
                    filmes[nomeFilme].qtd-=1
                    files[nomeFilme].reservados += 1
                    c.filmesReservados[nomeFilme] = {filmeReservar.titulo:filmeResevar, "DataAluguel": "%d-%d-%d" %(dataAluguel.date,dataAluguel.month,dataAluguel.year), "Situação":"Pendente, devendo R$%.2f" %(valor)}
                    c.debito += valor
            return "Reserva efetuada com exito. Valor a ser pago: ", valor, True         
                
        else:
            return "Nenhum Filme selecionado esta disponível para reserva!", False
        
        

    def aluguelreserv(nomeCliente = None, cpfCliente = None):
        clientes = shelve.open("clientes.pyc") #Clientes eh o ARQUIVO

        for c in clientes:
            if clientes[c].nome == nomeCliente:
                if cpfCliente != None and clientes[c].cpf == cpfCliente:
                    c = clientes[c]
                    break
                else:
                    return "Erro! CPF nao especificado ou congruencia entre CPF/Nome nao encontrada.", False


        if c.filmesReservados[nomeFilme]["DataAluguel"] == date.today():
            for nomeFilme in c.filmesReservados:
                dataDevolucao = date.fromordinal(date.toordinal(dataAluguel)+len(c.filmesReservados)) #Data na qual o DVD esta sendo alugado baseado na quantidade de filmes reservados
               
                if diaDevolucao == 6:
                    dataDevolucao = date.fromordinal(date.toordinal(dataDevolucao)+1)
                    
                c.filmesAlugados[nomeFilme] = c.filmesReservados[nomeFilme]
                c.filmesAlugados[nomeFilme]["DataDevolucao"] = "%d-%d-%d" %(dataDevolucao.date,dataDevolucao.month,dataDevolucao.year)           
            c.filmesReservados = {}
            return "Aluguel efetuado com exito", valor, True 
        else:
            return "Filme reservado para o dia: ",c.filmesReservados[nomeFilme]["DataAluguel"], False
       
    def aluguel(self,CarrinhodeCompras = None, nomeCliente = None, cpfCliente = None):
        if CarrinhodeCompras == None:
            return "Erro! Produtos não especificados",False
        if len(CarrinhodeCompras) == 0:
            wx.MessageBox("Erro! Nenhum produto selecionado")
        #Verifica se o usuario preencheu a forma de pagamento
        
        filmes = shelve.open("filmes")
        clientes = shelve.open("clientes") #Clientes eh o ARQUIVO

        if clientes.has_key(nomeCliente.upper()):
            if cpfCliente != None and clientes[c].cpf == cpfCliente:
                c = clientes[c]
            else:
                wx.MessageBox("Erro! CPF nao especificado ou congruencia entre CPF/Nome nao encontrada.")
                return
        valor = self.TotalPagar(CarrinhodeCompras)
        if len(CarrinhodeCompras)>0:
            dataAluguel = date.today()
            dataDevolucao = date.fromordinal(date.toordinal(dataAluguel)+len(CarrinhodeCompras)) #Data na qual o DVD esta sendo alugado
            diaDevolucao = dataDevolucao.weekday()

            if diaDevolucao == 6:
                dataDevolucao = date.fromordinal(date.toordinal(dataDevolucao)+1)
                
            for prod in CarrinhodeCompras:
                if filmes[prod.titulo].qtd != 0:
                    filmes[prod.titulo].quantidade-=1
                    filmeAlugar = filmes[prod.titulo]
                    del filmeAlugar.quantidade
                    filmeAlugar.dataAluguel="%d-%d-%d" %(dataAluguel.day,dataAluguel.month,dataAluguel.year)
                    filmeAlugar.dataDevolucao="%d-%d-%d" %(dataDevolucao.day,dataDevolucao.month,dataDevolucao.year)
                    c.filmesAlugados[filmeAlugar.titulo] = filmeAlugar
                    c.situacao = "DEBITO"
                    c.debito += valor
            wx.MessageBox("Aluguel efetuado com exito. Valor a ser pago: %.2f" %(valor))         
                
        else:
            wx.MessageBox("Nenhum Filme selecionado esta disponível no estoque!")

    def TotalPagar(self,Carrinho):
        valor = 0
        for prod in range(0,len(Carrinho)):
            valor += Carrinho[prod].valor
        return valor
    
    def pagamento(valor = None, nomeCliente = None, cpfCliente = None):
        if valor == None:
            return "Falha no processamento do débito",False
        if nomeCliente == None or cpfCliente == None:
            return "Cliente ou CPF não especificado(s)",False
        
        clientes = shelve.open("clientes.pyc") 

        for c in clientes:
            if clientes[c].nome == nomeCliente:
                if cpfCliente != None and clientes[c].cpf == cpfCliente:
                    c = clientes[c]
                    break
                else:
                    return "Erro! CPF nao especificado ou congruencia entre CPF/Nome nao encontrada.", False

        c.debito -= valor
        if c.debito == 0:
            c.situacao = True
        return "Pagamento realizado com sucesso", True
        

    def devolucao(nomeCliente = None,cpfCliente = None, valor=None):
        if nomeCliente == None or cpfCliente == None:
            return "Cliente ou CPF não especificado(s)",False
        
        clientes = shelve.open("clientes.pyc") 

        for c in clientes:
            if clientes[c].nome == nomeCliente:
                if cpfCliente != None and clientes[c].cpf == cpfCliente:
                    c = clientes[c]
                    break
                else:
                    return "Erro! CPF nao especificado ou congruencia entre CPF/Nome nao encontrada.", False

        if c.debito != 0:
            c.debito -= valor

        if c.debito == 0:
            c.situacao == True

        c.filmesAlugados = {}
        return "Operação concluída",True

