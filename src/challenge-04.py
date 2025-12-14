"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo"""

from datetime import date

todaysDate = date.today()
currentYear = todaysDate.year

yearOfBirth = int(input("Enter your year of birth: "))
age = currentYear - yearOfBirth
print(f"Quem nasceu em {yearOfBirth} tem {age} anos em {currentYear}")

if age < 18:
  alista = 18 - age
  print(f"Ainda faltam {18 - age} anos para o alistamento")
  print(f"Seu alistamento será em {currentYear + (18 - age)}")
elif age > 18:
  print(f"Você já deveria ter se alistado há {age - 18}")
  print(f"Seu alistamento foi em {currentYear - (age - 18)}")
else:
  print("Você tem que se alistar imediatamente")