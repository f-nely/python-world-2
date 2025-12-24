"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo"""

number1 = int(input("Enter a number: "))

qtdDivisores = 0
for i in range(1, number1 + 1):
  if number1 % i == 0:
    qtdDivisores += 1 
    print(i, end=" ")

print(f"\nO número {number1} foi divisível {qtdDivisores} vezes")
if qtdDivisores == 2:
  print("E por isso ele é primo")
else:
  print("E por isso ele não é primo")