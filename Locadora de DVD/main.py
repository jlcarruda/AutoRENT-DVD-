#!usr/bin/python
#_*_ coding:utf-8 _*_
# MAIN.PY --- Funcoes e Classes mais pertinentes em relacao ao programa
#    modulos para execucao em segundo plano
#

#___METAS_________-
#   - Implementar a conta do valor de acordo com Dia da Semana e Categoria
#   - Terminar metodo de "devolucao"
#   -

from cliente import cliente
from produto import produto
import shelve
from datetime import date

def cadastrarFilme(codigo = None, titulo = None, qtd = None):
    lista = [codigo, titulo, qtd]
    if (filter(lambda a: a==None, lista)) == True or type(qtd) != int:
        # Se existir algum campo nao preenchido ou a quantidade nao for digitada, retornar Falso.
        return "Ocorreu um erro! Verifique os campos de texto", False
    elif qtd < 0:
        return "Valor de Quantidade com formato Intrabalhavel.", False
    dataHj = "%d/%d/%d" %(date.today.day(), date.today.month(), date.today.year())
    p = produto(titulo, codigo, qtd, dataHj)
    filmes = shelve.open("filmes")
    filmes[p.titulo] = p
    filmes.close()
    return "Cadastro de filme concluido.", True

def cadastrarClientes(nome = None, CPF = None):
    if nome == None or CPF == None:
        return "Ocorreu um erro! Voce esqueceu de digitar um dos campos acima.", False
    else:
        c = cliente(nome, CPF)
        clientes = shelve.open("clientes","c")
        clientes[c.nome.upper()] = c
        clientes.close()
        return "Cadastro de cliente concluido.", True

def removerCliente(nome = None):
    if nome != None:
        clientes = shelve.open("clientes.txt")
        if clientes.has_key(nome):
            if clientes[nome].situacao == True:
                del clientes[nome]
                return "Cliente removido.", True
            else:
                return "Cliente em debito!", False
        else:
            return "Cliente nao encontrado!", False
    else:
        return "Preencha os campos obrigatorios", False

# PROCURA O CLIENTE EM "clientes.txt" por CPF e por Nome
def __procurarClienteCPF(cpfCliente = None):
    clientes = shelve.open("clientes")
    #Verifica se os espacos nao foram preenchidos pelo usuario
    if cpfCliente == None:
        return False
    #Procura pelo nome
    for x in clientes:
        if clientes[x].cpf == cpfCliente:
            return clientes[x]
    else:
        return False

def carrinho(objetoFilme):
    return

def __procurarFilme():
    return

def aluguel(codigo = None, nomeFilme = None, pagamentoAgora = None, nomeCliente = None, cpfCliente = None):
    #Dados persistentes ao Calculo do valor do aluguel do DVD.
    valor = 0
    diaSemana = ["Segunda", "Terca","Quarta","Quinta","Sexta","Sabado","Domingo"]
    valorRaw = [6.0,6.0,6.0,6.0,6.0,8.5,8.5]
    listaux = [codigo, nomeFilme, pagamentoAgora]
    #Verifica se o usuario preencheu a forma de pagamento
    if pagamentoAgora == None:
        return "Erro! Defina a forma do pagamento ou digite uma quantidade."
    preenchidos = filter(lambda a: a!=None, listaux)
    filmes = shelve.open("filmes.txt")
    clientes = shelve.open("clientes.txt") #Clientes eh o ARQUIVO

    for c in clientes:
        if clientes[c].nome == nomeCliente:
            if cpfCliente != None and clientes[c].cpf == cpfCliente:
                c = clientes[c]
                break
            else:
                return "Erro! CPF nao especificado ou congruencia entre CPF/Nome nao encontrada.", False

    dataAluguel = date.today()
    dataDevolucao = date.fromordinal(date.toordinal(dataAluguel)) #Data na qual o DVD esta sendo alugado
    diaDevolucao = dataDevolucao.weekday()

    if diaDevolucao == 6:
        dataDevolucao = date.fromordinal(date.toordinal(dataDevolucao)+1)
        pass

    elif nomeFilme in preenchidos:
        nomeFilme = nomeFilme.upper()
        if filmes.has_key(nomeFilme):    #Verifica se o nome esta digitado
            if filmes[nomeFilme].qtd != 0:
                filmes[nomeFilme].qtd-=1
                filmeAlugar = filmes[nomeFilme]
                del filmeAlugar.qtd
                c.filmesAlugados[filmeAlugar.nome] = {filmeAlugar.titulo:filmeAlugar, "DataAluguel": "%d-%d-%d" %(dataAluguel.date,dataAluguel.month,dataAluguel.year), "DataDevolucao":"%d-%d-%d" %(dataDevolucao.date,dataDevolucao.month,dataDevolucao.year), "Situação":"Pendente, devendo R$%.2f" %(valor)}
                return "Aluguel efetuado com exito", True
            else:
                return "Filme nao disponivel no estoque.", False
    elif codigo in preenchidos:
        for x in filmes:
            if filmes[x].codigo == codigo:
                if filmes[x].qtd != 0:
                    filmes[x].qtd-=1
                    filmeAlugar = filmes[x]
                    del filmeAlugar.qtd
                    c.filmesAlugados[filmeAlugar.nome] = {filmeAlugar.titulo:filmeAlugar, "DataAluguel": "%d-%d-%d" %(dataAluguel.date,dataAluguel.month,dataAluguel.year),"DataDevolucao":"%d-%d-%d" %(dataDevolucao.date,dataDevolucao.month,dataDevolucao.year), "Situação":"Pendente, devendo R$%.2f" %(valor)}
                    return "Aluguel efetuado com exito", True
                else:
                    return "Filme nao disponivel no estoque.", False
    else:
        return "Nome e Codigo do Filme nao especificado!", False


def devolucao(codigo = None, nomeCliente = None, cpfCliente = None, nomeFilme = None):
    listaux = [codigo, nomeCliente.upper(), nomeFilme.upper(), cpfCliente]
    if (codigo != None or nomeFilme != None) and (nomeCliente != None or cpfCliente != None):
        filmes = shelve.open("filmes")
        clientes = shelve.open("clientes")
        if clientes.has_key(nomeCliente.upper()):
            if clientes[nomeCliente.upper()]["Status"]["Filmes"].has_key(nomeFilme.upper()):
                return









