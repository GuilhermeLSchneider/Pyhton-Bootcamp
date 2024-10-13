class Produto:
    def __init__(self, nome, preco = 1.99, desc=0):
        self.nome = nome 
        self.__preco = preco # Os caracteres "__" trasnsformam esse atributo em um atributo privado
        self.desc = desc
    
    @property
    def get_preco(self):
        return self.__preco
    
    @get_preco.setter
    def set_preco(self, valor):
        if valor > 0:
            self.__preco = valor
    
    @property
    # Essa nomenclatura permite que um método seja chamado como um atributo e não mais como um método
    def preco_com_desconto(self):
        return self.get_preco * (1 - self.desc)

p1 = Produto('Camiseta', 50, 0.1)
p2 = Produto('Iphone', 10000, 0.15)

p1.set_preco = 100

print(p1.nome, p1.get_preco, p1.preco_com_desconto)
print(p2.nome, p2.get_preco, p2.preco_com_desconto)