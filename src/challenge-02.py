"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
-1 para binário
-2 para octal
-3 para hexadecimal
"""

dec = int(input("Enter an integer number: "))
print("Select one of the bases for conversion:")
print("[1] Convert to binary")
print("[2] Convert to octal")
print("[3] Convert to hexadecimal")

opt = int(input("Your choice: "))
if opt == 1:
  print(f"{dec} converted to binary is {bin(dec)[2:]}")
elif opt == 2:
  print(f"{dec} converted to octal is {oct(dec)[2:]}")
elif opt == 3:
  print(f"{dec} converted to hexadecimal is {hex(dec)[2:]}")
else:
  print("Invalid option")