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
# - Decidir o que fazer com a ideia de Autenticação ----- >[OK]

# - Exibir os dados de Procura de Filmes ----------> 
# ----- Exibir dados filtrados por Categoria e Midia 
# ----- Exibir dados filtrados por Titulo e Codigo -----> [OK]

# - Exibir os dados de Procura de Clientes --------> [OK]
# - Adicionar e Implementar os Botoes de "Remover Cliente" e "Remover Filme"(ADM Sensitive)
# - Adicionar e Implementar os Botoes de "Alugar" e "Devolver"
# - Opcional -- Adicionar um menu Float nos items da lista para Facilitar operacoes


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
ID_ADMLOGOUT=992
ID_TELCLIENTE = 9903
ID_ADDCARRINHO=9999
ID_CLEARCARRINHO=9429

class carrinho:
    carrinhoDeCompras ={}
    index=0
    def add(self, filme):
        self.carrinhoDeCompras[filme.titulo] = filme
        for x in carrinhoDeCompras:
            janela.CarrinhoList.InsertStringItem(self.index,self.carrinhoDeCompras[x].codigo)
            janela.CarrinhoList.SetStringItem(self.index,1,self.carrinhoDeCompras[x].titulo)
            janela.CarrinhoList.SetStringItem(self.index,2,self.carrinhoDeCompras[x].midia)
            janela.CarrinhoList.SetStringItem(self.index,3,str(self.carrinhoDeCompras[x].quantidade))
    def clear(self):
       self.carrinhoDeCompras={}
       for x in carrinhoDeCompras:
            janela.CarrinhoList.InsertStringItem(self.index,self.carrinhoDeCompras[x].codigo)
            janela.CarrinhoList.SetStringItem(self.index,1,self.carrinhoDeCompras[x].titulo)
            janela.CarrinhoList.SetStringItem(self.index,2,self.carrinhoDeCompras[x].midia)
            janela.CarrinhoList.SetStringItem(self.index,3,str(self.carrinhoDeCompras[x].quantidade))

##############################################################################################################
class JanelaPrincipal(wx.Frame):
    AdminLogged=False
    AdminPass = 'jrrtolkien'
    listaDeItems = []
    item=[]
    index=0
    listaDeClientes = []
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self,parent,wx.ID_ANY,title=title, size=(1024,768),
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
        File.AppendSeparator()
        File.Append(ID_ADMLOGOUT, "ADM %LogOut", "Desloga da conta de ADM")

        Carrinho = wx.Menu()

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
        self.Bind(wx.EVT_MENU, self.OnRemoverCliente, id=ID_REMOVERC)
        self.Bind(wx.EVT_MENU, self.ADMCheck, id=ID_ADMLOGOUT)

        # -- CARRINHO DE COMPRAS ------------------------------------
        wx.StaticBox(self.Painel,-1,'Carrinho De Compras',(630,10),(370,680))

        self.CarrinhoLista = wx.ListCtrl(self.Painel,ID_CARRINHO,(640,30),(350,650),style=wx.LC_REPORT|wx.SUNKEN_BORDER)

        self.CarrinhoLista.InsertColumn(1234,'Codigo')
        self.CarrinhoLista.InsertColumn(234,'Titulo',width=100)
        self.CarrinhoLista.InsertColumn(553,'Midia')
        self.CarrinhoLista.InsertColumn(4234,'Quantidade')

        wx.Button(self.Painel,id=ID_ALUGAR,label="Alugar Filmes no Carrinho",pos=(450,172), size=(140,-1))
        wx.Button(self.Painel,id=ID_ADDCARRINHO, label="Adicionar ao Carrinho",pos=(450,212),size=(140,-1))
        wx.Button(self.Painel,id=ID_CLEARCARRINHO, label="Limpar Carrinho",pos=(450,252),size=(140,-1))
        

        # -- STATIC BOX CLIENTES ------------------------------------
        
        wx.StaticBox(self.Painel,-1,'Dados do Cliente',(10,10),(600,130))
        wx.StaticText(self.Painel,-1,'Nome: ',(20,30))
        wx.StaticText(self.Painel,-1,'CPF: ', (20,70))
        wx.StaticText(self.Painel,-1,'Telefone: ',(20,110))

        self.NomeCliente =wx.TextCtrl(self.Painel,ID_NOMECLIENTE,'',(90,27),(200,-1))
        self.cpfCliente = wx.TextCtrl(self.Painel, ID_CPFCLIENTE,'',(90,67),(100,-1))
        self.TelCliente = wx.TextCtrl(self.Painel, ID_TELCLIENTE,'',(90,107),(100,-1))

        self.BotaoRemoverCliente = wx.Button(self.Painel,id=ID_REMOVERC, label="Remover Cliente",pos=(300,85), size=(140,-1))
        
        wx.Button(self.Painel,id=ID_SEARCHCLIENTS,label="Procurar Cliente",pos=(300,25),size=(140,-1))
        wx.Button(self.Painel,id=ID_CADASTROC, label='Cadastro de Cliente', pos=(300,55),size=(140,-1))

        # -- STATIC BOX FILMES --------------------------------------
        wx.StaticBox(self.Painel,-1,'Dados do Filme',(10,145),(600,150))
        wx.StaticText(self.Painel,-1,'Titulo: ',(20,165))
        wx.StaticText(self.Painel,-1,'Categoria: ',(20,195))
        wx.StaticText(self.Painel,-1,'Codigo: ',(20,225))
        wx.StaticText(self.Painel,-1,'Midia: ',(20,255))

        wx.Button(self.Painel, id=ID_SEARCHMOVIES, label="Procurar Filme", pos=(300,172), size=(140,-1))
        wx.Button(self.Painel, id=ID_ADDM, label="Cadastrar Filme", pos=(300,212), size=(140,-1))

        self.Titulo = wx.TextCtrl(self.Painel,ID_TITULO,'',(90,162),(200,-1))
        self.Categoria = wx.ComboBox(self.Painel,ID_CATEGORIA,'',(90,192),(100,-1),choices = ['','Lancamento','Catalogo','Super Lancamento'],
                        style=wx.CB_READONLY|wx.CB_SORT)
        self.Codigo = wx.TextCtrl(self.Painel,ID_CODIGO,'',(90,222),(100,-1))
        self.Midia = wx.ComboBox(self.Painel,ID_MIDIACOMBO,'',(90,252),(100,-1),choices=['','DVD','Blueray','Games'],
                                 style=wx.CB_READONLY|wx.CB_SORT)

        self.Quantidade = wx.TextCtrl(self.Painel,1234,'',(280,253),(50,-1))
        self.TextEstoque= wx.StaticText(self.Painel,-1,'Estoque: ',(220,253))

        if self.AdminLogged == True:
            pass
        else:
            self.BotaoRemoverCliente.Show(False)
            self.TextEstoque.Show(False)
            self.Quantidade.Show(False)
            
        # -- ListCtrl PARA RESULTADOS DE BUSCA ---------------
        wx.StaticBox(self.Painel,-1,'Resultado de Busca de Filmes',(10,300),(600,180))

        self.ResultadoMovie=wx.ListCtrl(self.Painel,ID_SHOWMOVIESLIST,(20,320),(580,150),style=wx.LC_REPORT|wx.SUNKEN_BORDER)
       
        ID_ESTOQUE=10
        ID_MIDIA=14
        ID_TITULODATA = 1467
        ID_CATEGORIADATA = 1232
        ID_CODIGODATA = 6545
                
        self.ResultadoMovie.InsertColumn(ID_CODIGODATA,'Codigo',width=60)
        self.ResultadoMovie.InsertColumn(ID_TITULODATA, 'Titulo',width=200)
        self.ResultadoMovie.InsertColumn(ID_CATEGORIA, 'Categoria',width=100)
        self.ResultadoMovie.InsertColumn(ID_ESTOQUE, 'Estoque',width=70)
        self.ResultadoMovie.InsertColumn(ID_MIDIA, 'Midia',width=70)
        self.ResultadoMovie.InsertColumn(1234,'Reservados')

        wx.StaticBox(self.Painel,-1,'Clientes',(10,480),(600,250))

        self.ResultadoCliente=wx.ListCtrl(self.Painel,ID_SHOWCLIENTSLIST,(20,500),(580,180),style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.ResultadoCliente.InsertColumn(11,'Nome do Cliente',width=160)
        self.ResultadoCliente.InsertColumn(12,'CPF',width=100)
        self.ResultadoCliente.InsertColumn(13,'Situacao',width=100)
        self.ResultadoCliente.InsertColumn(14,'Debito')
        self.ResultadoCliente.InsertColumn(15,'Telefone',width=100)
        
        self.ItemTabela={}
        

        # -- EVENT HANDLERS BUTTONS ----------------------

        self.Bind(wx.EVT_BUTTON, self.OnButtomCadastroFilme, id=ID_ADDM)
        self.Bind(wx.EVT_BUTTON, self.OnCadastrarCliente, id=ID_CADASTROC)
        self.Bind(wx.EVT_BUTTON, self.OnMostrarClientes, id=ID_SEARCHCLIENTS)
        self.Bind(wx.EVT_BUTTON, self.OnButtomProcurarFilme, id=ID_SEARCHMOVIES)
        self.Bind(wx.EVT_BUTTON, self.OnRemoverCliente, id=ID_REMOVERC)
        self.Bind(wx.EVT_BUTTON, self.OnAlugar, id=ID_ALUGAR)


    def OnAlugar(self,evento):
        return
    def OnAddCarrinho(self,evento):
        if self.ResutadoMovie.GetItemCount()>0:
            wx.MessageBox("Filtre os filmes o suficiente para que esteja apenas um deles na lista")
        else:
            item = self.ResultadoMovie.GetTopItem()
            carrinho.add(item)
            wx.MessageBox("Item Adicionado ao Carrinho")
            
    #---------------------------------------------------------------------------------------------------------------------
    def GetItemSelecionado(self):
         '''get the currently focused item or -1 if none'''
         return self.GetNextItem(-1, wx.LIST_NEXT_ALL,
            wx.LIST_STATE_FOCUSED)
    #-------------------------------------------------------------------------------------------------------------------    
    def ADMCheck(self,evento):
        if self.AdminLogged==False:
            wx.MessageBox('Operacao Invalida','Error',wx.OK|wx.ICON_ERROR)
        else:
            self.AdminLogged=False
            self.Painel.Hide()
            self.Quantidade.Show(False)
            self.TextEstoque.Show(False)
            self.BotaoRemoverCliente.Show(False)
            self.Painel.Show()
            wx.MessageBox('ADM Deslogado com Sucesso!','Info',wx.OK|wx.ICON_INFORMATION)
    #---------------------------------------------------------------------------------------------------------------------        
    def OnExit(self, evento):
        self.Close(True)
    #---------------------------------------------------------------------------------------------------------------------
    def OnButtomProcurarFilme(self,evento):
        self.TituloStr = str(self.Titulo.GetValue())
        self.MidiaStr = str(self.Midia.GetValue())
        self.CategoriaStr = str(self.Categoria.GetValue())
        self.CodigoStr = str(self.Codigo.GetValue())
        self.index = 0
        self.listaObj = []
        self.ResultadoMovie.DeleteAllItems()
        try:    
            self.listaDeItems = loja.procurarFilme(self.TituloStr, self.CodigoStr, self.CategoriaStr, self.MidiaStr)
            for x in range(0,len(self.listaDeItems)):
                self.ResultadoMovie.InsertStringItem(self.index,self.listaDeItems[x].codigo)
                self.ResultadoMovie.SetStringItem(self.index,1,self.listaDeItems[x].titulo)
                self.ResultadoMovie.SetStringItem(self.index,2,self.listaDeItems[x].categoria)
                self.ResultadoMovie.SetStringItem(self.index,3,str(self.listaDeItems[x].quantidade))
                self.ResultadoMovie.SetStringItem(self.index,4,self.listaDeItems[x].midia)
                self.ResultadoMovie.SetStringItem(self.index,5,str(self.listaDeItems[x].reservados))
                self.index+=1
        except:
            wx.MessageBox('Erro de busca!', 'Erro[211]',wx.OK|wx.ICON_ERROR)
    #---------------------------------------------------------------------------------------------------------------------
    def OnButtomCadastroFilme(self,evento):
        if self.AdminLogged==True:
            self.TituloStr = str(self.Titulo.GetValue())
            self.MidiaStr = str(self.Midia.GetValue())
            self.CodigoStr = str(self.Codigo.GetValue())
            self.QuantidadeStr = int(self.Quantidade.GetValue())
            self.CategoriaStr = str(self.Categoria.GetValue())
            try:
                if (self.TituloStr == self.CodigoStr) and (self.MidiaStr == self.TituloStr) and self.CodigoStr==self.MidiaStr and self.TituloStr=='':
                    wx.MessageBox('Dados não preenchidos corretamente','Info',wx.OK|wx.ICON_EXCLAMATION)
                    return False
                loja.cadastroFilme(self.TituloStr,self.CodigoStr,self.QuantidadeStr,self.MidiaStr,self.CategoriaStr)
                self.Titulo.Clear()
                self.Codigo.Clear()
                wx.MessageBox('Filme Cadastrado com Sucesso','Info',wx.OK|wx.ICON_INFORMATION)
            except:
                wx.MessageBox('Erro! Nao foi possivel continuar o cadastro!', 'Error', wx.OK | wx.ICON_ERROR)
        if self.AdminLogged==False:
            janelaAuth=JanelaDeAutenticacao(janela)
            janelaAuth.Show()
            janelaAuth.Center()
    #---------------------------------------------------------------------------------------------------------------------   
    def OnCadastrarCliente(self,evento):
        self.NomeStr = str(self.NomeCliente.GetValue())
        self.CPF = str(self.cpfCliente.GetValue())
        self.Tel = str(self.TelCliente.GetValue())
        if self.NomeStr == self.CPF or self.NomeStr=='' or self.CPF =='' or self.Tel=='':
            wx.MessageBox('Dados nao preenchidos corretamente', 'Info',wx.OK|wx.ICON_EXCLAMATION)
            return False
        try:
            loja.cadastroCliente(self.NomeStr, self.CPF, self.Tel)
            wx.MessageBox('Cliente Cadastrado com sucesso','Info',wx.OK|wx.ICON_INFORMATION)
        except:
            wx.MessageBox('Erro ao tentar cadastrar o Cliente','Error',wx.OK|wx.ICON_ERROR)
    #---------------------------------------------------------------------------------------------------------------------
    def OnRemoverCliente(self,evento):
        if self.AdminLogged:
            self.NomeStr = str(self.NomeCliente.GetValue())
            self.CPF = str(self.cpfCliente.GetValue())
            if self.NomeStr == self.CPF or self.NomeStr=='' or self.CPF =='':
                wx.MessageBox('Dados nao preenchidos corretamente', 'Info',wx.OK|wx.ICON_EXCLAMATION)
                return False
            try:
                loja.removerCliente(self.NomeStr,self.CPF)
            except:
                pass

        else:
            janelaAuth=JanelaDeAutenticacao(janela)
            janelaAuth.Show()
            janelaAuth.Center()
    #---------------------------------------------------------------------------------------------------------------------
    def OnRemoverFilmes(self,evento):
        if self.AdminLogged:
            self.TituloStr = str(self.Titulo.GetValue())
            self.CodigoStr = str(self.Codigo.GetValue())
            if self.TituloStr == self.CodigoStr or self.TituloStr=='':
                wx.MessageBox('Dados nao preenchidos corretamente', 'Info',wx.OK|wx.ICON_EXCLAMATION)
                return False
            '''
                Aqui vai o codigo para Remover o Cliente
            '''

        else:
            janelaAuth=JanelaDeAutenticacao(janela)
            janelaAuth.Show()
            janelaAuth.Center()
    #---------------------------------------------------------------------------------------------------------------------
    def OnMostrarFilmes(self, evento):
        self.ResultadoMovie.DeleteAllItems()
        try:
            self.listaDeItems = loja.procurarFilme('','','','')
            for x in range(0,len(self.listaDeItems)):
                self.ResultadoMovie.InsertStringItem(self.index,self.listaDeItems[x].codigo)
                self.ResultadoMovie.SetStringItem(self.index,1467,self.listaDeItems[x].titulo)
                self.ResultadoMovie.SetStringItem(self.index,2,self.listaDeItems[x].categoria)
                self.ResultadoMovie.SetStringItem(self.index,3,str(self.listaDeItems[x].quantidade))
                self.ResultadoMovie.SetStringItem(self.index,4,self.listaDeItems[x].midia)
                self.ResultadoMovie.SetStringItem(self.index,3,str(self.listaDeItems[x].reservas))
                self.index+=1
        except:
            wx.MessageBox('Erro ao tentar completar a busca por Filmes no Banco de Dados', 'Erro', wx.OK | wx.ICON_ERROR)
    #---------------------------------------------------------------------------------------------------------------------
    def OnMostrarClientes(self, evento):
        # Basicamente vai chamar o Procurar Cliente e mostrar na tela, loja.ProcurarCliente(nomeCliente, CPF)
        self.NomeStr = str(self.NomeCliente.GetValue())
        self.CPF = str(self.cpfCliente.GetValue())
        self.ResultadoCliente.DeleteAllItems()
        self.index=0
        try:
            self.listaDeClientes = loja.procurarCliente(self.NomeStr, self.CPF)
            for x in range(0,len(self.listaDeClientes)):
                self.ResultadoCliente.InsertStringItem(self.index,self.listaDeClientes[x].nome)
                self.ResultadoCliente.SetStringItem(self.index,1,self.listaDeClientes[x].cpf)
                self.ResultadoCliente.SetStringItem(self.index,2,self.listaDeClientes[x].situacao)
                self.ResultadoCliente.SetStringItem(self.index,3,str(self.listaDeClientes[x].debito))
                self.ResultadoCliente.SetStringItem(self.index,4,self.listaDeClientes[x].tel)
                self.index += 1
                
        except:
            wx.MessageBox('Erro ao visualizar os Clientes','Error[300]',wx.OK|wx.ICON_ERROR)
#####################################################################################################################################
class JanelaDeAutenticacao(wx.Frame):
    ErrorCount = 0
    #---------------------------------------------------------------------------------------------------------------------
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,wx.ID_ANY,title="AutoRENT DVD Auth",size=(200,80),
                          style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN )
        self.Painel=wx.Panel(self)
        wx.StaticText(self.Painel,-1,"Admin Pass: ",(20,20))
        self.Pass=wx.TextCtrl(self.Painel,ID_PASS,'',(90,17),(80,-1),style=wx.TE_PROCESS_ENTER| wx.TE_PASSWORD)

        self.Bind(wx.EVT_TEXT_ENTER, self.OnEnter, id=ID_PASS)        
    #---------------------------------------------------------------------------------------------------------------------
    def OnEnter(self,evento):
        self.PassStr = str(self.Pass.GetValue())
        if self.PassStr == janela.AdminPass:
            janela.AdminLogged=True
            janela.Painel.Hide()
            janela.Quantidade.Show(True)
            janela.TextEstoque.Show(True)
            janela.BotaoRemoverCliente.Show(True)
            janela.Painel.Show()
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
########################################################################################################################################
def alterarestado (self):
    today = "%s/%s/%s" %(str(date.today().day),str(date.today().month), str(date.today().year))
    
    if self.estado == 1:
        return "Erro! Filme selecionado classificado como catálogo",False
    elif self.estado == 1.5 and today == date.fromordinal(date.toordinal(self.dataCadastro)+60):
        self.estado -= 0.25
        return "Estado do filme alterado com sucesso",True
    elif self.estado == 1.25 and today == date.fromordinal(date.toordinal(self.dataCadastro)+240):
        return "Estado do filme alterado com sucesso",True
        self.estado -= 0.25
    else:
        return "Filme fora da data de mudança de classificação",False
if __name__ == '__main__':
    app = wx.App()
    loja = loja()
    carrinho=carrinho()
    janela = JanelaPrincipal(parent = None, id=ID_JANELA,title="AutoRENT DVDs Beta 0.8v")
    janela.Center()
    janela.Show()
    app.MainLoop()



