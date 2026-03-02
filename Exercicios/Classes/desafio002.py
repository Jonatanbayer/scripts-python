from rich import print
from rich.panel import Panel
from rich.align import Align
class Produto:
    '''
    permite cadastrar um produto e mostrar sua etiqueta de preço
    '''
    def __init__(self, nome = str, preco = float):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        #return f'Produto: {self.nome}, Preço: R${self.preco:.2f}'
        painel = Panel(Align.center(f'{self.nome}\nR${self.preco:,.2f}'), title='Produto', style='blue', width=50)
        return painel

    
prod1 = Produto('Shampoo', 2.99)
print(prod1.etiqueta())
prod2 = Produto('Headset', 30.59)
print(prod2.etiqueta())