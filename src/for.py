"""Estrutura de repetição for"""

""" for i in range(0, 12, 2):
  print(i)
print("The end") """

""" n = int(input("Type a number: "))
for i in range(0, n + 1):
  print(i) """

""" beginning = int(input("Beginning: "))
theEnd = int(input("The end: "))
step = int(input("Step: "))

for i in range(beginning, theEnd + 1, step):
  print(i)
print("The end") """

s = 0
for i in range(0, 4):
  value = int(input("Type a value: "))
  s += value
print(f"O somátorio é {s}")