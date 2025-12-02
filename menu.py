from banco import Banco
from conta import Conta
from Cartao import Cartao
banco = Banco("Banco")
banco.criar_conta("001","NuBank","Thaís",1000)
banco.criar_conta("002","Inter","Lucas",500)
banco.criar_conta("003","C6","Maria",1500)
banco.criar_conta("004","Banco do Brasil","João",2000)
banco.criar_conta("005","Caixa","Ana",2500)

print("------------------------------------")
print("---Bem-vindo ao sistema bancário!---")
print("------------------------------------")

print("Você é...")
print("1- Cliente")
print("2- Funcionário do banco")

opcao = int(input("Digite 1 ou 2:"))
if opcao == 1:
  ID = input("Bem-vindo! Digite o ID da sua conta:")
  
