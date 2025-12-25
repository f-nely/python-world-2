"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
A média de idade do grupo;
Qual é o nome do homem mais velho
Quantas mulheres têm menos de 20 anos"""

averageAge = 0
nameOfOlderMan = ""
ageOlderMan = 0
numbersOdWomen = 0
ages = 0
for i in range(1, 5):
  print(f"----- {i}ª Pessoa -----")
  name = str(input("Nome: ")).strip()
  age = int(input("Idade: "))
  gender = str(input("Sexo [M/F]: ")).upper()
  
  # Somátorio idade
  ages += age  

  if i == 1 and gender in "Mn":
    ageOlderMan = age
    nameOfOlderMan = name
  if gender in "Mn" and age > ageOlderMan:
    ageOlderMan = age
    nameOfOlderMan = name
  """ if gender in "Mm" and age > ageOlderMan:
    ageOlderMan = age
    nameOfOlderMan = name """
  if gender in "Ff" and age < 20:
    numbersOdWomen += 1

averageAge = ages / 4
print(f"A média da idade do grupo é de {averageAge:.1f}")
print(f"O homem mais velho tem {ageOlderMan} anos e se chama {nameOfOlderMan}")
print(f"Ao todo são {numbersOdWomen} mulheres com menos de 20 anos")