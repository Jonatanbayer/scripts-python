from rich import print
from rich import inspect
class Banco:
    '''
    Cria uma conta bancária e permite fazer depósitos e saques!
    '''
    def __init__(self, id = int, titular = str, saldo = float):
        self.id = id
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f'[bold blue on white]Atualmente a conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo[/]'
    
    def deposito(self, valor_deposito = float):
        self.saldo += valor_deposito
        print(f'O valor de R${valor_deposito:,.2f} foi depositado')
    
    def saque(self, valor_saque = float):
        if valor_saque < self.saldo:
            self.saldo -= valor_saque
            return print(f'O valor de R${valor_saque:,.2f} foi sacado')
        else:
             return print(f'[red]Saldo insuficiente![/], a conta atualmente possui o saldo de R${self.saldo:,.2f}')

conta_1 = Banco(331, 'Arnaldo', 3500.99)
print(conta_1.__str__())
conta_1.deposito(3000)
print(conta_1.__str__())
conta_1.saque(10000)
inspect(conta_1)
