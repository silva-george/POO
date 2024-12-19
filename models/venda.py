import json
import datetime

class Venda:
    def __init__(self, id, data, carrinho, total, id_cliente):
        self.id = id # atributos de instância
        self.data = data
        self.carrinho = carrinho
        self.total = total
        self.id_cliente = id_cliente

    def __str__(self):
        return f"Id: {self.id} - Data: {self.data} - Total: R${self.total:.2f}"

class Vendas:
    objetos = [] # atributo de classe
    @classmethod
    def criar(cls, obj):
        # abre a lista do arquivo
        cls.abrir()
        # calcula o id do objeto
        id = 0
        for x in cls.objetos:
            if x.id > id: id = x.id
        obj.id = id + 1    
        # insere o objeto na lista
        cls.objetos.append(obj)
        # salva a lista no arquivo
        cls.salvar()
    @classmethod
    def listar(cls):
        # abre a lista do arquivo
        cls.abrir()
        # retorna a lista para a UI
        return cls.objetos[:]
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        # percorre a lista procurando o id    
        for x in cls.objetos:
            if x.id == id: return x
        return None
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()        
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.salvar()
    
    @classmethod
    def fechar(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            x.carrinho = False
            cls.salvar()

    @classmethod
    def atualizar_total(cls, venda, valor):
        x = cls.listar_id(venda.id)
        if x != None:
            x.total = x.total + valor
            cls.salvar()
    
    @classmethod
    def mostrar_total(cls, id):
        x = cls.listar(id)
        if x != None:
            return x.total
        

    @classmethod
    def salvar(cls):
        # open - cria e abre o arquivo clientes.json
        # vars - converte um objeto em um dicionário
        # dump - pega a lista de objetos e salva no arquivo
        with open("vendas.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        # esvazia a lista de objetos
        cls.objetos = []
        try:
            with open("vendas.json", mode="r") as arquivo:
                # abre o arquivo com a lista de dicionários -> clientes_json
                objetos_json = json.load(arquivo)
                # percorre a lista de dicionários
                for obj in objetos_json:
                    # recupera cada dicionário e cria um objeto
                    c = Venda(obj["id"], obj["data"], obj["carrinho"], obj["total"], obj["id_cliente"])
                    # insere o objeto na lista
                    cls.objetos.append(c)    
        except FileNotFoundError:
            pass
    

