class Conta():
  def __init__(self, id,saldo,senha):
    self.id = id 
#    self.banco = banco 
#    self.titular = titular
    self.saldo = 0.0
    self.saldo = saldo
    self.senha = senha
  
  def depositar(self,valor):
    if valor>0:
      self.saldo+= valor
      print("Depósito realizado com sucesso!")
    else:
      print("Depósito não realizado! O valor do depósito precisa ser maior que 0")
  
  def sacar(self, valor):
    if self.saldo >= valor:
      if valor>0:
        self.saldo-=valor
        print("Saque realizado com sucesso!")
      else:
        print("Saque não realizado! O valor do saque precisa ser maior que 0")
    else: 
      print("Saldo insuficiente!")
  
  def ver_saldo(self):
    print(f"Seu saldo é de R${self.saldo}")
  

# Depois fazer o Extrato