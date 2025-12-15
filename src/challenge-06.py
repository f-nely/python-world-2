"""A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
Até 9 anos: mirim
Até 14 anos: infantil
Até 19 anos: junior
Até 25 anos: sênior
Acima: master"""

from datetime import date

currentYear = date.today().year

yearOfBirth = int(input("Enter your year of birth: "))
age = currentYear - yearOfBirth

print(f"The athlete is {age} years old")
if age <= 9:
  print("Classification: mirim")
elif age <= 14:
  print("Classification: infantil")
elif age <= 19:
  print("Classification: junior")
elif age <= 25:
  print("Classification: sênior")
else:
  print("Classification: master")