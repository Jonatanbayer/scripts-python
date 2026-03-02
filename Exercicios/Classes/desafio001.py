class Funcionario:
    '''
    permite cadastrar uma pessoa como funcionario e apresentar sua função na empresa
    '''
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self):
        return f'Olá meu nome é {self.nome}, sou {self.cargo} no setor de {self.setor}'
    
func1 = Funcionario('Carine', 'Vendas', 'Vendedor')
print(func1.apresentar())
func2 = Funcionario('Anthony', 'negócios', 'gerente')
print(func2.apresentar())