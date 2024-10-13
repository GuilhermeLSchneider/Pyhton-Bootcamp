
class Contador:
    contador = 0

    # Esse método não pode ser acessado sem criar uma instância da classe
    def inst(self):
        return 'Objeto criado'

    # É utilizado para fazer com que métodos sejam utilizados sem criar uma instância da classe
    @classmethod
    def incrementar(self):
        self.contador += 1
        return self.contador

    @classmethod
    def decrementar(self):
        self.contador -= 1
        return self.contador

    # É utilizado para criar métodos que não acessam os atributos da classe
    @staticmethod
    def dividir_por_2(valor):
        return valor / 2

    def mostrar(self):
        print(self.valor)

# Contador.inst() => Não é possível acessar

Contador.incrementar()
Contador.incrementar()
Contador.incrementar()
print(Contador.incrementar())

print(Contador.dividir_por_2(50))