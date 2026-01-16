"""Faça um programa que leia um número qualquer e mostre o seu fatorial"""

# from math import factorial

num = int(input("Enter a number: "))
# print(factorial(num))

""" print(f"Calculando {num}! =", end=" ") 
j = num
fat = 1
while j >= 1:
  print(f"{j} ", end="")
  if j > 1:
    print("x ", end="")
  else:
    print("= ", end="")
  fat *= j
  j -= 1

print(f"{fat}") """

fat = 1
print(f"Calculando o fatoria {num}! =", end=" ")
for i in range(num, 0, -1):
  print(f"{i} ", end="")
  if i > 1:
    print("x ", end="")
  else:
    print("= ", end="")
  fat *= i

print(fat)
  