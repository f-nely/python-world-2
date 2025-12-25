"""Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos"""

greaterWeight = 0
lowerWeight = 0
for i in range(1, 6):
  weight = float(input(f"Peso {i}ª pessoa: "))
  if i == 1:
    greaterWeight = weight
    lowerWeight = weight
  else:
    if weight > greaterWeight:
      greaterWeight = weight
    if weight < lowerWeight:
      lowerWeight = weight

print(f"O maior peso lido foi {greaterWeight}Kg")
print(f"O menor peso lido foi {lowerWeight}Kg")
  