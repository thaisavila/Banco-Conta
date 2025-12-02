from conta import Conta
from banco import Banco

class Cartao(Conta):
  def __init__(self,limite,total_gasto,id,saldo,senha):
    self.limite = limite
    self.total_gasto = 0.0
    super().__init__(saldo,id,senha)

  def compra_credito(self,valor):
    if valor<=self.limite:
      print(f"Compra de R${valor} aprovada no crédito!")
      self.total_gasto = self.total_gasto + valor
    else: 
      print("Compra recusada! Limite excedido.")
  
  def compra_debito(self, valor):
    if valor>self.saldo:
      print("Compra recusada! Saldo insuficiente.")
    else:
      self.saldo = self.saldo - valor
      print("Compra no débito efetuada com sucesso!")

  def ver_limite(self):
    print(f"Seu limite total é R${self.limite}")
    print(f"Você utilizou R${self.total_gasto} do limite")
    print(f"Seu limite restante é R$ {self.limite - self.total_gasto}")

  def pagar_fatura(self):
    if self.saldo >= self.total_gasto:
      self.saldo = self.saldo - self.total_gasto
      self.total_gasto = 0
      print("Pagamento de fatura efetuado com sucesso!")
    else:
      print("Saldo Insuficiente!")

cartao = Cartao(2000, 0, 3000, 100, "1234")
cartao.ver_limite()  # usa instância!
cartao.compra_credito(500)
cartao.ver_limite()  # veja o resultado
