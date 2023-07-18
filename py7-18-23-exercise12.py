#Crie uma classe chamada BankAccount (Conta Bancária) que tenha os métodos deposit (depósito), withdraw (saque) e get_balance (saldo). 
# Garanta que o saldo não possa ser acessado diretamente fora da classe, mas possa ser atualizado por meio dos métodos deposit e withdraw. 
# Implemente também um método display_balance (exibir saldo) que exiba o saldo atual. Teste sua classe realizando depósitos, saques e exibindo o saldo.

class BankAccount():
        def __init__(self):
                self.saldo = 0
        def deposit(self,deposit):
                self.saldo += deposit
        def withdraw(self,saque):
                self.saldo -= saque
        def display_balance(self):
                print("O valor de sua conta é "+str(self.saldo))

conta = BankAccount()

for i in range(1,100):
        x = int(input("Insira 1-Para ver o valor em sua conta\nInsira 2-Para realizar depósitos\nInsira 3-Para realizar saques"))
        if x == 1:
                conta.display_balance()
        elif x == 2:
                y = float(input("Insira o valor para depósito"))
                conta.deposit(y)
                conta.display_balance()
        elif x == 3:
                y = float(input("Insira o valor de saque"))
                conta.withdraw(y)
                conta.display_balance()