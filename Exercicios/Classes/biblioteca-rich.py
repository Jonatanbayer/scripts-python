from rich import print
from rich.panel import Panel
from rich.table import Table
#from rich.traceback import install
#install() -- Torna os erros do código mais legivel e compreensivel

caixa = Panel('Esse aqui é um painel de exemplo', title='Mensagem', style='red')
print(caixa)

tabela = Table(title='Tabela de preços')

tabela.add_column('Nome')
tabela.add_column('Preço')
tabela.add_column('Data')

tabela.add_row('Lápis', 'R$1.50', '27-02-26')
print(tabela)