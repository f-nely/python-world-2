"""Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o"""

accumulator = 0
counter = 0
for i in range(0, 6):
  n = int(input("Enter a number: "))
  if n % 2 == 0:
    counter += 1
    accumulator += n 

print(f"Você digitou {counter} números pares e a soma foi {accumulator}")