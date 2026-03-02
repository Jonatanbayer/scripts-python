#declaração de classe:
class classe:
    '''
    Documentação da classe!
    '''
    #declaração atributos
    def __init__(self, nome, idade): #método construtor
        self.nome = nome
        self.idade = idade
    #métodos
    def aniversario(self):
        self.idade += 1
    def mensagem(self):
        return f'{self.nome} tem {self.idade} anos de idade'

#declaração de objetos:
obj = classe('jonatan', 23) #instanciação

print(obj.mensagem())
print(classe.__doc__)
print(obj.__dict__)