"""Crie um programa que leia dois valores e mostre um menu como o ao lado na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
O programa deverá realizar a operação solicitada em cada caso"""

from time import sleep

value1 = int(input("First value: "))
value2 = int(input("Second value: "))

opt = 0
while opt != 5:
  print(
  """
  [1] somar
  [2] multiplicar
  [3] maior
  [4] novos números
  [5] sair do programa
  """)
  opt = int(input(">>>>>> What is your option? "))
  if opt == 1:
    print(f"A soma entre {value1} + {value2} é {value1 + value2}")
  elif opt == 2:
    print(f"A multiplicação entre {value1} * {value2} é {value1 * value2}")
  elif opt == 3:
    if value2 > value1:
      largestNumber = value2
    elif value1 > value2:
      largestNumber = value1
    print(f"Entre {value1} e {value2} o maior valor é {largestNumber}")
  elif opt == 4:
    print("Enter the numbers again: ")
    value1 = int(input("First value: "))
    value2 = int(input("Second value: "))
  elif opt == 5:
    print("Ending...")
  else:
    print("Invalid option! Try again")
  print("=-=" * 10)
  sleep(2)
print("The end of the program")
    
