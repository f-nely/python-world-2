"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas jão são maiores"""

from datetime import date
currentYear = date.today().year

minor = 0
legalAge = 0
for i in range(1, 8):
  yearOfBirth = int(input(f"In what year was the {i}ª person born? ")) 
  age = currentYear - yearOfBirth
  if age < 18:
    minor += 1
  else:
    legalAge += 1

print(f"Ao todo tivemos {legalAge} pessoas maiores de idade")
print(f"E também tivemos {minor} pessoas menores de idade")
