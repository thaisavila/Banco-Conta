from conta import Conta

class Banco():
  def __init__(self,nome):
    self.nome = nome
    self.contas = []

  def criar_conta(self,id,banco,titular,saldo):
    nova_conta = Conta(id,banco,titular,saldo)
    self.contas.append(nova_conta)
    print("Conta criada com sucesso!")
    return nova_conta
  
  def listar_contas(self):
    if len(self.contas) == 0:
      print("Nenhuma conta cadastrada.")
    else:
      for conta in self.contas:
        print(f"ID: {conta.id}, Titular: {conta.titular}, banco: {conta.banco} Saldo: R${conta.saldo}")
  
  def buscar_conta(self,id):
      for conta in self.contas:
        if conta.id == id:
          print(f"ID: {conta.id}, Titular: {conta.titular}, banco: {conta.banco}, Saldo: R${conta.saldo}")
        return
  print("Conta não encontrada.")

  def transferir(self, id_origem, id_destino, valor):
    conta_origem = None
    conta_destino = None

    for conta in self.contas:
      if conta.id == id_origem:
        conta_origem = conta
      if conta.id == id_destino:
        conta_destino = conta

    if conta_origem is None:
      print("Conta de origem não encontrada.")
      return
    if conta_destino is None:
      print("Conta de destino não encontrada.")
      return
    if valor <= 0:
      print("O valor da transferência deve ser maior que 0.")
      return
    if conta_origem.saldo < valor:
      print("Saldo insuficiente na conta de origem.")
      return

    conta_origem.sacar(valor)
    conta_destino.depositar(valor)
    print("Transferência realizada com sucesso!")

  def saldo_total(self):
    total = 0.0
    for conta in self.contas:
      total += conta.saldo
    
    print(f"O saldo total do banco é R${total}")

# Apagar conta
