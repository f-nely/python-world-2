"""Melhore o jogo do desafio 28 no qual o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer"""

from random import randint
secretNumber = randint(1, 10)

print("""Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?
""", end="")

qtdPalpites = 1
chosenNumber = int(input("Qual seu palpite? "))

while secretNumber != chosenNumber:
  if chosenNumber > secretNumber:
    print("Menos... Tente mais uma vez.")
  elif chosenNumber < secretNumber:
    print("Mais... Tente mais uma vez")
  chosenNumber = int(input("Qual seu palpite? "))
  qtdPalpites += 1

print(f"Acertou com {qtdPalpites} tentativas. Parabéns!")

