from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput
import main, cliente, produto


with PyCallGraph(output = GraphvizOutput(output_file = "teste.png")):
    loja = main()
    loja.cadastrarCliente("Lucas", "10398690413")
    loja.cadastrarFilme(002,"Star Wars 1",7)