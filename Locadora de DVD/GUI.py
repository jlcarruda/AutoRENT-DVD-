#_*_coding:utf-8_*_
#-------------------------------------------------------------------------------
# Name:        GUI.py
# Purpose:      Toda a modelagem da GUI do programa
# Version:      0.0.1 ALPHA
# Author:      Joao Lucas de Carvalho Arruda
#
# Created:     01/11/2013
# Copyright:   (c) JoaoLucasDeCarvalhoArruda 2013
# Licence:     *************
#-------------------------------------------------------------------------------

# Metas
# - Decidir o que fazer com a ideia de Autenticação
# - Adicionar os botões de Procura/Cadastro Cliente
# - Exibir os dados de Procura


import wx
from main1 import *

ID_CARRINHOJANELA = 1001
ID_CARRINHO = 1000
ID_JANELA = 999
ID_ADDM = 101
ID_DELM = 102
ID_CADASTROC = 1234
ID_REMOVERC = 4321
ID_SEARCHCLIENTS = 103
ID_SEARCHMOVIES = 104
ID_SHOWMOVIES = 105
ID_SHOWCLIENTS = 106
ID_EXIT = 107
ID_DEVOLVER = 108
ID_ALUGAR = 109
ID_StaticNome = 8323
ID_NOMECLIENTE = 110
ID_CPFCLIENTE = 111
ID_TITULO = 112
ID_CODIGO = 113
ID_CATEGORIA = 114
ID_PAINELCL = 115
ID_BUTAOPROCURAFILME = 116
ID_BUTAOCADASTROFILME=444
ID_MIDIACOMBO = 117
ID_PASS=435
ID_SHOWMOVIESLIST = 675
ID_SHOWCLIENTSLIST = 678

AdminLogged=False
AdminPass = 'jrrtolkien'

class JanelaPrincipal(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self,parent,wx.ID_ANY,title=title, size=(800,600),
             style= wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN | wx.NO_FULL_REPAINT_ON_RESIZE)
        # -- PAINEL ---------------------------------------
        self.Painel = wx.Panel(self)

        # -- Barra de STATUS ------------------------------
        self.CreateStatusBar()
        self.SetStatusText(str(date.today()))
        # -- Menu SUPERIOR -----------------------------------
        menuSup = wx.MenuBar()

        File = wx.Menu()

        File.Append(ID_SHOWMOVIES,"Mostrar &Filmes", "Mostra a lista de todos os filmes Cadastrados")
        File.Append(ID_SHOWCLIENTS,"Mostrar &Clientes", "Mostra lista de todos os clientes Cadastrados")
        File.AppendSeparator()
        File.Append(ID_EXIT, "&Exit", "Fecha o Programa")

        Carrinho = wx.Menu()

        Carrinho.Append(ID_CARRINHOJANELA, "Abrir Carrinho", "Abre a janela do Carrinho de Compras")
        Carrinho.AppendSeparator()
        Carrinho.Append(ID_ADDM, "&Add Filmes", "Adiciona Filmes ao Carrinho")
        Carrinho.Append(ID_DELM, "&Del Filmes", "Remove Filmes do Carrinho")

        CadastroeRemocao = wx.Menu()

        CadastroeRemocao.Append(ID_CADASTROC,"Cadastrar Cliente", "Cadastra o Cliente no Sistema")
        CadastroeRemocao.Append(ID_REMOVERC, "Deletar Cliente", "Deleta o Cliente no Sistema")
        
        menuSup.Append(File,"File")
        menuSup.Append(Carrinho, "Carrinho")
        menuSup.Append(CadastroeRemocao, "Cadastro e Remocao")
        self.SetMenuBar(menuSup)

        # -- EVENT HANDLERS MENU BAR -----------------------------------
        self.Bind(wx.EVT_MENU, self.OnExit, id=ID_EXIT)
        self.Bind(wx.EVT_MENU, self.OnButtomCadastroFilme, id=ID_ADDM)
        self.Bind(wx.EVT_MENU, self.OnRemoverFilmes, id=ID_DELM)
        self.Bind(wx.EVT_MENU, self.OnMostrarClientes, id=ID_SHOWCLIENTS)
        self.Bind(wx.EVT_MENU, self.OnMostrarFilmes, id=ID_SHOWMOVIES)
        self.Bind(wx.EVT_MENU, self.OnCadastrarCliente, id=ID_CADASTROC)

        # -- STATIC BOX CLIENTES ------------------------------------
        wx.StaticBox(self.Painel,-1,'Dados do Cliente',(10,10),(450,80))
        wx.StaticText(self.Painel,ID_StaticNome,'Nome: ',(20,30))
        wx.StaticText(self.Painel,2,'CPF: ', (20,60))

        wx.Button(self.Painel,id=ID_SEARCHCLIENTS,label="Procurar Cliente",pos=(300,25),size=(140,-1))
        wx.Button(self.Painel,id=ID_CADASTROC, label='Cadastro de Cliente', pos=(300,55),size=(140,-1))

        # -- STATIC BOX FILMES --------------------------------------
        wx.StaticBox(self.Painel,-1,'Dados do Filme',(10,95),(450,150))
        wx.StaticText(self.Painel,4,'Titulo: ',(20,115))
        wx.StaticText(self.Painel,5,'Categoria: ',(20,145))
        wx.StaticText(self.Painel,6,'Codigo: ',(20,175))
        wx.StaticText(self.Painel,7,'Midia: ',(20,205))

        wx.Button(self.Painel, id=ID_SEARCHMOVIES, label="Procurar Filme", pos=(300,122), size=(140,-1))
        wx.Button(self.Painel, id=ID_ADDM, label="Cadastrar Filme", pos=(300,162), size=(140,-1))

        # -- ComboBox, SpinCtrl e TxtCtrl -------------------
        self.NomeCliente =wx.TextCtrl(self.Painel,ID_NOMECLIENTE,'',(90,27),(200,-1))
        self.cpfCliente = wx.TextCtrl(self.Painel, ID_CPFCLIENTE,'',(90,57),(100,-1))

        self.Titulo = wx.TextCtrl(self.Painel,ID_TITULO,'',(90,112),(200,-1))
        self.Categoria = wx.ComboBox(self.Painel,ID_CATEGORIA,'',(90,142),(100,-1),choices = ['Lancamento','Catalogo','Super Lancamento'],
                        style=wx.CB_READONLY|wx.CB_SORT)
        self.Codigo = wx.TextCtrl(self.Painel,ID_CODIGO,'',(90,172),(100,-1))
        self.Midia = wx.ComboBox(self.Painel,ID_MIDIACOMBO,'',(90,202),(100,-1),choices=['DVD','Blueray','Games'],
                                 style=wx.CB_READONLY|wx.CB_SORT)

        #self.Quantidade = wx.TextCtrl(self.Painel,1234,'',(90,230),(100,-1))
        
        # -- ListCtrl PARA RESULTADOS DE BUSCA ---------------
        wx.StaticBox(self.Painel,-1,'Resultado de Busca de Filmes',(10,250),(380,230))

        self.ResultadoMovie=wx.ListCtrl(self.Painel,ID_SHOWMOVIESLIST,(20,270),(360,200),style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.ResultadoMovie.Show(True)
        self.ResultadoMovie.InsertColumn(7,'Codigo')
        self.ResultadoMovie.InsertColumn(8, 'Titulo')
        self.ResultadoMovie.InsertColumn(9, 'Categoria')
        self.ResultadoMovie.InsertColumn(10, 'Estoque')

        wx.StaticBox(self.Painel,-1,'Clientes',(400,250),(380,230))

        self.ResultadoCliente=wx.ListCtrl(self.Painel,ID_SHOWCLIENTSLIST,(410,270),(360,200),style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.ResultadoCliente.Show(True)
        self.ResultadoCliente.InsertColumn(11,'Nome do Cliente')
        self.ResultadoCliente.InsertColumn(12,'CPF')
        self.ResultadoCliente.InsertColumn(13,'Situacao')        
        

        # -- EVENT HANDLERS BUTTONS ----------------------

        self.Bind(wx.EVT_BUTTON, self.OnButtomCadastroFilme, id=ID_ADDM)

    def OnExit(self, evento):
        self.Close(True)

    def OnButtomProcurarFilme(self,evento):
        return

    def OnButtomCadastroFilme(self,evento):
        if AdminLogged==True:
            self.TituloStr = str(self.Titulo.GetValue())
            self.MidiaStr = str(self.Midia.GetValue())
            self.CodigoStr = str(self.Codigo.GetValue())
            self.Quantidade=10
            try:
                loja.cadastroFilme(self.TituloStr,self.CodigoStr,self.Quantidade,self.MidiaStr)
                self.Titulo.Clear()
                self.Codigo.Clear()
                self.Midia.Clear()
            except:
                wx.MessageBox('Erro! Nao foi possivel continuar o cadastro!', 'Error', wx.OK | wx.ICON_ERROR)
        if AdminLogged==False:
            janelaAuth=JanelaDeAutenticacao(janela)
            janelaAuth.Show()
            janelaAuth.Center()
       
    def OnCadastrarCliente(self,evento):
        return
    def OnRemoverCliente(self,evento):
        return
    def OnRemoverFilmes(self,evento):
        return

    def OnMostrarFilmes(self, evento):
        # Chama o loja.ProcurarFilme(nomeFilme, codigo) e retorn a o resultado
        try:
            loja.procurarFilmes(self.Titulo,self.Codigo, self.Categoria)
        except:
            wx.MessageBox('Erro!', 'Info', wx.OK | wx.ICON_ERROR)

    def OnMostrarClientes(self, evento):
        # Basicamente vai chamar o Procurar Cliente e mostrar na tela, loja.ProcurarCliente(nomeCliente, CPF)
        self.NomeClienteStr = janela.NomeCliente.GetStringSelection()
        self.cpfClienteStr = janela.cpfCliente.GetValue()
        try:
            loja.procurarClientes(self.NomeClienteStr, self.cpfClienteStr)
        except:
            wx.MessageBox('Erro! Falta de Dados para Busca!', 'Info', wx.OK | wx.ICON_ERROR)


class JanelaDeAutenticacao(wx.Frame):
    ErrorCount = 0
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,wx.ID_ANY,title="AutoRENT DVD Auth",size=(200,80),
                          style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN )
        self.Painel=wx.Panel(self)
        wx.StaticText(self.Painel,-1,"Admin Pass: ",(20,20))
        self.Pass=wx.TextCtrl(self.Painel,ID_PASS,'',(90,17),(80,-1),style=wx.TE_PROCESS_ENTER| wx.TE_PASSWORD)

        self.Bind(wx.EVT_TEXT_ENTER, self.OnEnter, id=ID_PASS)        

    def OnEnter(self,evento):
        self.PassStr = str(self.Pass.GetValue())
        if self.PassStr == AdminPass:
            global AdminLogged
            AdminLogged=True
            wx.MessageBox('Logado em Administrador!','Acesso Permitido!',wx.OK | wx.ICON_INFORMATION)
            self.Destroy()
        else:
            self.ErrorCount+=1
            if self.ErrorCount>2:
                wx.MessageBox('Acesso Negado! Voce tentou obter acesso privilegiado 3 vezes!','Acesso Negado!',wx.OK | wx.ICON_ERROR)
                self.Destroy()
                return
            wx.MessageBox('Senha incorreta!','Auth Error',wx.OK | wx.ICON_ERROR)
            self.Pass.Clear()
        
if __name__ == '__main__':
    app = wx.App()
    loja = loja()
    carrinho=carrinho()
    janela = JanelaPrincipal(parent = None, id=ID_JANELA,title="AutoRENT DVDs")
    janela.Center()
    janela.Show()
    app.MainLoop()



