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
        self.Bind(wx.EVT_MENU, self.OnAddFilmes, id=ID_ADDM)
        self.Bind(wx.EVT_MENU, self.OnDelFilmes, id=ID_DELM)
        self.Bind(wx.EVT_MENU, self.OnMostrarClientes, id=ID_SHOWCLIENTS)
        self.Bind(wx.EVT_MENU, self.OnMostrarFilmes, id=ID_SHOWMOVIES)
        self.Bind(wx.EVT_MENU, self.OnCadastrarCliente, id=ID_CADASTROC)

        # -- STATIC BOX CLIENTES ------------------------------------
        wx.StaticBox(self.Painel,-1,'Dados do Cliente',(10,10),(450,80))
        wx.StaticText(self.Painel,ID_StaticNome,'Nome: ',(20,30))
        wx.StaticText(self.Painel,2,'CPF: ', (20,60))

        # -- STATIC BOX FILMES --------------------------------------
        wx.StaticBox(self.Painel,-1,'Dados do Filme',(10,95),(450,150))
        wx.StaticText(self.Painel,4,'Titulo: ',(20,115))
        wx.StaticText(self.Painel,5,'Categoria: ',(20,145))
        wx.StaticText(self.Painel,6,'Codigo: ',(20,175))
        wx.StaticText(self.Painel,7,'Midia: ',(20,205))

        wx.Button(self.Painel, id=ID_BUTAOPROCURAFILME, label="Procurar Filme", pos=(300,122), size=(140,-1))
        wx.Button(self.Painel, id=ID_BUTAOCADASTROFILME, label="Cadastrar Filme", pos=(300,162), size=(140,-1))

        # -- ComboBox, SpinCtrl e TxtCtrl -------------------
        self.NomeCliente =wx.TextCtrl(self.Painel,ID_NOMECLIENTE,'',(90,27),(200,-1))
        self.cpfCliente = wx.TextCtrl(self.Painel, ID_CPFCLIENTE,'',(90,57),(100,-1))

        self.Titulo = wx.TextCtrl(self.Painel,ID_TITULO,'',(90,112),(200,-1))
        self.Categoria = wx.ComboBox(self.Painel,ID_CATEGORIA,'',(90,142),(100,-1),choices = ['Lancamento','Catalogo','Super Lancamento'],
                        style=wx.CB_READONLY|wx.CB_SORT)
        self.Codigo = wx.TextCtrl(self.Painel,ID_CODIGO,'',(90,172),(100,-1))
        self.Midia = wx.ComboBox(self.Painel,ID_MIDIACOMBO,'',(90,202),(100,-1),choices=['DVD','Blueray','Games'],
                                 style=wx.CB_READONLY|wx.CB_SORT)

        self.Quantidade = wx.TextCtrl(self.Painel,1234,'',(90,230),(100,-1))
        # -- ListCtrl PARA RESULTADOS DE BUSCA ---------------
        wx.StaticBox(self.Painel,-1,'Resultado de Busca',(10,250),(380,230), style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.ResultadoMovie=wx.ListCtrl(self.Painel,-1,(20,270),(360,200))
        self.ResultadoMovie.InsertColumn(7,'Código')
        self.ResultadoMovie.InsertColumn(8, 'Titulo')
        self.ResultadoMovie.InsertColumn(9, 'Categoria')
        self.ResultadoMovie.InsertColumn(10, 'Estoque')
        self.ResultadoMovie.Show(True)

        # -- EVENT HANDLERS BUTTONS ----------------------

        self.Bind(wx.EVT_BUTTON, self.OnButtomCadastroFilme, id=ID_BUTAOCADASTROFILME)

    def OnExit(self, evento):
        self.Close(True)

    def OnAddFilmes(self, evento):
        return
    def OnDelFilmes(self, evento):
        return

    def OnButtomCadastroFilme(self,evento):
        self.TituloStr = str(self.Titulo.GetValue())
        self.MidiaStr = str(self.Midia.GetValue())
        self.CodigoStr = str(self.Codigo.GetValue())
        try:
            loja.cadastroFilme(self.TituloStr,self.CodigoStr,self.Quantidade.GetValue(),self.MidiaStr)
            self.Titulo.Clear()
            self.Codigo.Clear()
            self.Midia.Clear()
        except:
            wx.MessageBox('Erro! Nao foi possivel continuar o cadastro!', 'Error', wx.OK | wx.ICON_ERROR)
       
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
'''
class __JanelaDeAutenticacao(wx.Frame):
    self.AdminScreen=True
    self.OnAuthentication=True
    def __init__(self,id):
        wx.Frame.__init__(self,parent,wx.ID_ANY,title="AutoRENT DVD Authentication",size(100,100),
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN )
        self.Painel=wx.Panel(self)
        while self.OnAuthentication:
            if self.AdminScreen:
                '''
                
                
                
    def TelaAdmin():    
        wx.StaticText(self.Painel,-1,'Login: ',(20,60))
        wx.StaticText(self.Painel,-1,'Password: ',(20,80))
        wx.StaticText(self.Painel,-1,'Admin Authentication'(20,40))
        

if __name__ == '__main__':
    app = wx.App()
    loja = loja()
    carrinho=carrinho()
    janela = JanelaPrincipal(parent = None, id=ID_JANELA,title="AutoRENT DVDs")
    janelaCadastroFilme = JanelaCadastroFilme(parent = janela, id = 99999999)
    janela.Center()
    janela.Show()
    app.MainLoop()



