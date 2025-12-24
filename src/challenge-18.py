"""Crie um programa que leia uma frase qualquer e dig se ela é um palíndromo, desconsiderando os espaços"""
text = str(input("Enter a sentence: ")).strip().lower()
text = text.replace(" ", "")
invertText = text[::-1]

print(f"O inverso de {text} é {invertText}")
if text == invertText:
  print("Temos um palíndromo")
else:
  print("A frase digitada não é um palíndromo")