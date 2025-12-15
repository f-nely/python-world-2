"""Refaça o desario dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
Equilátero: todos os lados iguais
Isóscele: dois lados iguais
Escaleno: todos os lados diferentes"""

s1 = int(input("Enter the first side of the triangle: "))
s2 = int(input("Enter the second side of the triangle: "))
s3 = int(input("Enter the third side of the triangle: "))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
  print("O segmento acima pode formar um triângulo ", end="")
  if s1 == s2 and s2 == s3:
    print("Equilátero")
  elif s1 != s2 and s2 != s3 and s1 != s3:
    print("Escaleno") 
  else:
    print("Isóscele")
else:
  print("O segmento acima não pode formar um triângulo")