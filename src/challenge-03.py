"""Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma mensagem:
O primeiro valor é maior
O segundo valor é maior
Não existe valor maior, os dois são iguais"""

num1 = int(input("Type the first number: "))
num2 = int(input("Type the second number: "))

if num1 > num2:
  print("The first value is the greatest")
elif num2 > num1:
  print("The second value is the greatest")
else:
  print("Both are equal")