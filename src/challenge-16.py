"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão"""

firstTerm = int(input("Primeiro termo: "))
r = int(input("Razão: "))
# an = 1 + 2·(n – 1)
for i in range(1, 11):
  print(f"{firstTerm + r * (i - 1)}", end=" ➜ ")
print("Acabou")