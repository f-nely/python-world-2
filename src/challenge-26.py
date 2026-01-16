"""Refaça o desafio 51, lendo o primeiro termo e a razão de uma P.A., mostrando os 10 primeiros termos da progressão usando a estrutura while"""

print("Gerador de PA")
print("-=" * 10)

firstTerm = int(input("Primeiro termo: "))
r = int(input("Razão: "))

j = 1
term = firstTerm
while j <= 10:
  print(f"{term} ➜ ", end="")
  term += r
  j += 1
print("FIM")