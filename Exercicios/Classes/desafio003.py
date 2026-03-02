from rich import print
from rich.panel import Panel
from rich.align import Align

#consumo padrão: 400g por pessoa
#Preço: 82,40/KG
class Churrasco:
    '''
    Cadastre um número de pessoas e o preço da carne para descobrir quanto vai custar para cada membro e o quanto de carne será necessário comprar
    '''
    def __init__(self, qtd_pessoas = int):
        self.qtd_pessoas = qtd_pessoas

    def qtd_carne(self):
        qtd_total_carne = (self.qtd_pessoas * 400) / 1000
        return {'Frase': f'Será necessário comprar {qtd_total_carne:.1f}Kg de carne', 'Numero': qtd_total_carne}
    
    def preco(self):
        qtd_total_carne = self.qtd_carne()['Numero']
        preco_pessoa = (qtd_total_carne * 82.40) / self.qtd_pessoas
        return preco_pessoa
    
    def analisar(self):
        painel = Panel(f'O churrasco conta com {self.qtd_pessoas} pessoas\nCada participante comerá 0.4Kg e cada Kg custa R$82.40\nÉ recomendado comprar {self.qtd_carne()['Numero']}Kg de carne\nO custo total será de R${self.qtd_carne()['Numero'] * 82.40:.2f}\nCada pessoa deve pagar {self.preco()}', title='Churrasco', style='Blue')
        return painel

    
churrasco1 = Churrasco(15)
print(churrasco1.analisar())