#Exercicio 01
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
    def area(self):
        return self.largura * self.altura
    
    def perimetro(self):
        return ((2*self.largura)+(2*self.altura))
        
#Exercicio 02
class ContaBancaria:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 0
        
    def depositar(self, valor):
        self.saldo += valor
        print(f"{valor} adicionado a sua conta!")
        
    def sacar(self, valor):
        if(self.saldo < valor):
            print(f"Erro ao realizar saque, saldo insuficiente!")
        else:
            self.saldo -= valor
            print(f"{valor} sacado de sua conta")
            
    def ver_saldo(self):
        print(f"Seu saldo atual é de {saldo}")
        
#Exercicio 03
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Carro(Veiculo):
    def dirigir(self):
        print(f"Dirigindo um carro {self.marca} {self.modelo}")
        
class Moto(Veiculo):
    def dirigir(self):
        print(f"Dirigindo uma moto {self.marca} {self.modelo}")
        
        
#Exercicio 04
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def aumentar_salario(self, percentual):
        self.salario = self.salario * (1+(percentual/100))
        print(f"O salário de {self.nome} agora é de {self.salario}")
        
#Exercicio 05
class Animal:
    def falar(self):
        pass
    
class Cachorro(Animal):
    def falar(self):
        print("Au au")
        
class Gato(Animal):
    def falar(self):
        print("Miau")
        
#Exercicio 06
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def aumentar_estoque(self, numero):
        self.quantidade += numero
        print(f"O novo estoque é de {self.quantidade}")
        
    def vender(self, numero):
        if(self.quantidade < numero):
            print("Erro! A quantidade solicitade é maior que o estoque")
        else:
            self.quantidade -= numero
            print(f"Venda efetuada com sucesso. A nova quantidade é de {self.quantidade}")
    
    def __str__(self):
        return(f"Produto(nome: {self.nome}, preco: {self.preco}, estoque: {self.quantidade}")
            


#Resolucoes
#01
retangulo = Retangulo(10,5)
print(f"A área é: {retangulo.area()}")
print(f"O perímetro é: {retangulo.perimetro()}")

#02
conta = ContaBancaria("Joao")
conta.depositar(1000.0)
conta.sacar(1500.0)
conta.sacar(600.0)
conta.ver_saldo

#03
carro = Carro("Hyndai", "HB20")
moto = Moto("Honda", "CB300")
carro.dirigir()
moto.dirigir()

#04
funcionario = Funcionario("Fulano", 3000.0)
funcionario.aumentar_salario(20)

#05
cachorro = Cachorro()
cachorro.falar()
gato = Gato()
gato.falar()

#06
produto = Produto("Camisa", 10.0, 6)
produto.aumentar_estoque(5)
produto.vender(30)
produto.vender(2)

#07
print(produto)
