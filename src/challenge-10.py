"""Crie um programa que faça o computador jogar Jokenpô com você"""

from random import choice
from time import sleep

jokenpo = ["Pedra", "Papel", "Tesoura"]
computer = choice(jokenpo)

print("-=" * 15)
print("Pedra, Papel, Tesoura")
print("-=" * 15)

player = str(input("Qual é sua jogada? ")).capitalize()

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!")

print(f"Computador jogou {computer}")
print(f"Jogador jogou {player}")

if computer == "Pedra":
  if player == "Pedra":
    print("Empate")
  elif player == "Papel":
    print("Jogador vence")
  elif player == "Tesoura":
    print("Computador vence")
  else:
    print("Jogada inválida")
elif computer == "Papel":
  if player == "Pedra":
    print("Computador vence")
  elif player == "Papel":
    print("Empate")
  elif player == "Tesoura":
    print("Jogador vence")
  else:
    print("Jogada inválida")
elif computer == "Tesoura":
  if player == "Pedra":
    print("Jogador vence")
  elif player == "Papel":
    print("Computador vence")
  elif player == "Tesoura":
    print("Empate")
  else:
    print("Jogada inválida")