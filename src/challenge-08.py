"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu imc e mostre seu status, de acordo com a tabela abaixo:
Abaixo de 18.5: abaixo do peso
Entre 18.5 e 25: peso ideal
25 até 30: sobrepeso
30 até 40: obesidade
Acima de 40: obesidade mórbida"""

weight = float(input("What is your weight? (Kg) ")) 
height = float(input("What is your height? (m) "))
imc = weight / (height ** 2)

print(f"O IMC dessa pessoa é {imc:.1f}")

if imc < 18.5:
  print("Você está em abaixo do peso normal")
elif imc >= 18.5 and imc < 25:
  print("Parabéns, você está na faixa de peso normal")
elif imc >= 25 and imc < 30:
  print("Você está em sobrepeso")
elif imc >= 30 and imc < 40:
  print("Você está em obesidade")
elif imc >= 40:
  print("Você está em obesidade mórbida, cuidado!")