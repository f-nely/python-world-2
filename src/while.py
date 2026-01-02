# Estrutura de Repetição While

""" j = 1
while j < 10:
  print(j)
  j += 1
"""

""" n1 = 1
while n1 != 0:
  n1 = int(input("Enter a number: ")) """

""" answer = "Yes"
while answer == "Yes":
  n1 = int(input("Enter a number: "))
  answer = str(input("Do you want to continue? [Yes/No] ")).capitalize()
print("Fim!") """

n1 = 1
qtdImpares = 0
qtdPares = 0
while n1 != 0:
  n1 = int(input("Enter a number: "))
  if n1 != 0:
    if n1 % 2 == 0:
      qtdPares += 1
    else:
      qtdImpares +=1
print(f"Você digitou {qtdPares} números pares e {qtdImpares} números ímpares")
