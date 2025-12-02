# Sistema Bancário em Python

Este projeto é um **sistema bancário**, desenvolvido para praticar conceitos de **Programação Orientada a Objetos (POO)** em Python, utilizando as classes:  **Banco**, **Conta** e **Cartao**.

## Funcionalidades

### Classe `Conta`
* Criar conta com id, saldo e senha
* Depositar valores
* Sacar valores (com verificação de saldo e valor válido)
* Verificar saldo disponível

### Classe `Banco`

* Criar novas contas
* Listar contas cadastradas
* Buscar conta pelo ID
* Transferência entre contas
* Somar saldo total do banco

### Classe `Cartao` (herda de `Conta`)

* Definir limite do cartão
* Realizar compras no crédito e no débito
* Ver limite disponível
* Pagar fatura (desconta do saldo da conta se tiver saldo suficiente)

## Herança

A classe `Cartao` herda de `Conta` e utiliza `super()` dentro do construtor para aproveitar os atributos e métodos da classe pai.

Exemplo:

```python
class Cartao(Conta):
    def __init__(self, limite, total_gasto, id, saldo, senha):
        self.limite = limite
        self.total_gasto = 0.0
        super().__init__(saldo, id, senha)
```

## 📚 Melhorias Futuras

* Criar sistema de **extrato**
* Implementar **interface de menu** completa - já iniciada, mas ainda não finalizada

---