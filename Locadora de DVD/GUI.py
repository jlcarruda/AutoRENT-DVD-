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

        # -- EVENT HANDLERS -----------------------------------
        self.Bind(wx.EVT_MENU, self.OnExit, id=ID_EXIT)
        self.Bind(wx.EVT_MENU, self.OnAddFilmes, id=ID_ADDM)
        self.Bind(wx.EVT_MENU, self.OnDelFilmes, id=ID_DELM)
        self.Bind(wx.EVT_MENU, self.OnMostrarClientes, id=ID_SHOWCLIENTS)
        self.Bind(wx.EVT_MENU, self.OnMostrarFilmes, id=ID_SHOWMOVIES)
        self.Bind(wx.EVT_MENU, self.OnCadastrarCliente, id=ID_CADASTROC)

        # -- STATIC BOX CLIENTES ------------------------------------
        wx.StaticBox(self.Painel,-1,'Dados do Cliente',(10,10),(390,80))
        wx.StaticText(self.Painel,ID_StaticNome,'Nome: ',(20,30))
        wx.StaticText(self.Painel,2,'CPF: ', (20,60))

        # -- STATIC BOX FILMES --------------------------------------
        wx.StaticBox(self.Painel,-1,'Dados do Filme',(10,95),(390,110))
        wx.StaticText(self.Painel,4,'Titulo: ',(20,115))
        wx.StaticText(self.Painel,5,'Categoria: ',(20,145))
        wx.StaticText(self.Painel,6,'Codigo: ',(20,175))

        # -- ComboBox, SpinCtrl e TxtCtrl -------------------
        self.NomeCliente =wx.TextCtrl(self.Painel,ID_NOMECLIENTE,'',(90,27),(200,-1))
        self.cpfCliente = wx.TextCtrl(self.Painel, ID_CPFCLIENTE,'',(90,57),(100,-1))

        self.Titulo = wx.TextCtrl(self.Painel,ID_TITULO,'',(90,112),(200,-1))
        self.Categoria = wx.ComboBox(self.Painel,ID_CATEGORIA,'',(90,142),(100,-1),choices = ['Lancamento','Catalogo','Super Lancamento'],
                        style=wx.CB_READONLY|wx.CB_SORT)
        self.Codigo = wx.TextCtrl(self.Painel,ID_CODIGO,'',(90,172),(100,-1))

        # -- ListCtrl PARA RESULTADOS DE BUSCA ---------------
        wx.StaticBox(self.Painel,-1,'Resultado de Busca',(10,230),(380,230), style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.ResultadoMovie=wx.ListCtrl(self.Painel,-1,(20,250),(360,200))
        self.ResultadoMovie.InsertColumn(7,'Código')
        self.ResultadoMovie.InsertColumn(8, 'Titulo')
        self.ResultadoMovie.InsertColumn(9, 'Categoria')
        self.ResultadoMovie.InsertColumn(10, 'Estoque')
        self.ResultadoMovie.Show(True)

    def OnExit(self, evento):
        self.Close(True)

    def OnAddFilmes(self, evento):
        return
    def OnDelFilmes(self, evento):
        return

    def OnButtomCadastroFilme(self,evento):
        janelaCadastroFilme.Show()
        janelaCadastroFilme.Center()

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





# -- JANELA DE CADASTRO DE FILMES --------------------------------------------------------------------------------------------



class JanelaCadastroFilme(wx.Frame):                      # Classe da janela de Cadastro de Filmes
    ID_BUTAOCADASTRO=444
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,wx.ID_ANY,title="Cadastro de Filmes",size=(400,200),
        style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN | wx.NO_FULL_REPAINT_ON_RESIZE )

        self.Painel = wx.Panel(self)

        wx.StaticBox(self.Painel,-1,'Dados de Cadastro',(10,10),(360,150))

        # -- TITULO ----------------------------------
        wx.StaticText(self.Painel,-1,'Titulo: ',(20,40))
        self.Titulo=wx.TextCtrl(self.Painel,345,'',(70,37),(280,-1))


        # -- CODIGO ----------------------------------
        wx.StaticText(self.Painel,-1,'Codigo: ',(20,70))
        self.Codigo=wx.TextCtrl(self.Painel, 456,'',(70,67),(150,-1))

        # -- QUANTIDADE ------------------------------
        wx.StaticText(self.Painel,-1,'Quantidade: ',(20,100))
        self.Quantidade=wx.SpinCtrl(self.Painel,-1,'',min=1,max=99,pos=(90,97),size=(60,-1))

        # -- MIDIA -----------------------------------
        wx.StaticText(self.Painel,-1,'Midia: ',(20,130))
        self.Midia=wx.TextCtrl(self.Painel,-1,'',(70,127),(100,-1))

        wx.Button(self.Painel, id=self.ID_BUTAOCADASTRO, label="Cadastrar", pos=(250,127), size=(100,-1)) # CRIAÇAO NO BOTAO

        self.Bind(wx.EVT_BUTTON,self.OnCadastro,id=self.ID_BUTAOCADASTRO)

    def OnCadastro(self,evento):
        self.TituloStr = self.Titulo.GetValue()
        self.MidiaStr = self.Midia.GetValue()
        self.CodigoStr = self.Codigo.GetValue()

        loja.cadastroFilme(self.TituloStr,self.CodigoStr,self.Quantidade.GetValue(),self.MidiaStr)
        print self.TituloStr
        print self.MidiaStr
        print self.CodigoStr
        print self.Quantidade.GetValue()
        self.Titulo.Clear()
        self.Codigo.Clear()
        self.Midia.Clear()

if __name__ == '__main__':
    app = wx.App()
    loja = loja()
    carrinho=carrinho()
    janela = JanelaPrincipal(parent = None, id=ID_JANELA,title="AutoRENT DVDs")
    janelaCadastroFilme = JanelaCadastroFilme(parent = janela, id = 99999999)
    janela.Center()
    janela.Show()
    janelaCadastroFilme.Show()
    app.MainLoop()



