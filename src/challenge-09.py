"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
À vista dinheiro: 10% de desconto
À vista no cartão: 5% de desconto
Em até 2x no cartão: preço normal
Em 3x ou mais no cartão: 20% de juros"""

purchasePrice = float(input("What is the purchase price? R$"))
print(
"""Formas de Pagamento
[1] à vista dinheiro
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão"""
)
option = int(input("What is the option? "))
if option == 1:
  total = purchasePrice - (purchasePrice * 10 / 100)
elif option == 2:
  total = purchasePrice - (purchasePrice * 5 / 100)
elif option == 3:
  total = purchasePrice
  installment = purchasePrice / 2
  print(f"Sua compra será parcelana em 2x R$ {installment:.2f} sem juros")
elif option == 4:
  total = purchasePrice + (purchasePrice * 20 / 100)
  totalInstallment = int(input("how many installments? "))
  installment = total / totalInstallment
  print(f"Sua compra será parcelana em {totalInstallment}x de R${installment:.2f} com juros")
else: 
  total = purchasePrice
  print("Opção inválida")
print(f"Sua compra de R${purchasePrice:.2f} vai custar {total:.2f} no final")