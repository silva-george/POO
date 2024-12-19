import datetime
from models.cliente import Cliente, Clientes
from models.categoria import Categoria, Categorias
from models.produto import Produto, Produtos
from models.venda_item import VendaItem, VendasItens
from models.venda import Venda, Vendas

class View:
    @staticmethod
    def cliente_admin():
        for c in Clientes.listar():
            if c.email == "admin": return None
        View.cliente_inserir("admin", "admin", "0000", "1234")    
    @staticmethod
    def cliente_autenticar(email, senha):
        for c in Clientes.listar():
            if c.email == email and c.senha == senha:
                return { "id" : c.id, "nome" : c.nome }
        return None    

    @staticmethod
    def cliente_listar():
        return Clientes.listar()
    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        c = Cliente(0, nome, email, fone, senha)
        Clientes.inserir(c)
        venda = Venda(0, datetime.datetime.now().strftime("%d/%m/%Y"), True, 0, c.id)
        Vendas.criar(venda)
        print("Cliente", c.nome, "inserido com sucesso")
    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        c = Cliente(id, nome, email, fone, senha)
        Clientes.atualizar(c)
    @staticmethod
    def cliente_excluir(id):
        c = Cliente(id, "", "", "", "")
        Clientes.excluir(c)
        
#Categoria
    @staticmethod
    def categoria_listar():
        return Categorias.listar()
    @staticmethod
    def categoria_listar_id(id):
        return Categorias.listar_id(id)
    @staticmethod
    def categoria_inserir(descricao):
        c = Categoria(0, descricao)
        Categorias.inserir(c)
    @staticmethod
    def categoria_atualizar(id, descricao):
        c = Categoria(id, descricao)
        Categorias.atualizar(c)
    @staticmethod
    def categoria_excluir(id):
        c = Categoria(id, "")
        Categorias.excluir(c)

#Produto
    @staticmethod
    def produto_listar():
        return Produtos.listar()
    @staticmethod
    def produto_inserir(descricao, preco, estoque, id_categoria):
        c = Produto(0, descricao, preco, estoque, id_categoria)
        Produtos.inserir(c)
    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, id_categoria):
        c = Produto(id, descricao, preco, estoque, id_categoria)
        Produtos.atualizar(c)
    @staticmethod
    def produto_excluir(id):
        c = Produto(id, "", 0, 0, None)
        Produtos.excluir(c)
    @staticmethod
    def produto_reajustar(percentual):
        for obj in View.produto_listar():
            View.produto_atualizar(obj.id, obj.descricao, obj.preco * (1 + percentual), obj.estoque, obj.id_categoria)
    @staticmethod
    def produto_detalhe(id):
        return Produtos.detalhes(id)
    
#Venda    
    @staticmethod
    def criar_venda(id, data, carrinho, total, id_cliente):
        venda = Venda(id, data, carrinho, total, id_cliente)
        return Vendas.criar(venda)
    @staticmethod
    def venda_listar():
        return Vendas.listar()
    
    @staticmethod
    def fechar_venda(obj):
        return Vendas.fechar(obj)

    @staticmethod    
    def atualizar_total_venda(venda, total):
        Vendas.atualizar_total(venda, total)
#VendaItem        
    @staticmethod
    def inserir_produto_venda_item(id, qtd, preco, id_venda, id_produto):
        item = VendaItem(id, qtd, preco, id_venda, id_produto)
        VendasItens.inserir(item)

    @staticmethod
    def venda_item_listar():
        return VendasItens.listar()
    
    
