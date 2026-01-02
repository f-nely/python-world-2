"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto"""

gender = str(input("Informe seu sexo: [M/F] ")).strip().upper()[0]
while gender not in "MmFf":
  gender = str(input("Dados inválidos. Por favor informe seu sexo: ")).upper()
print(f"Sexo {gender} registrado com sucesso!") 
  

