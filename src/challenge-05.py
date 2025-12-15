"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
Média abaixo de 5.0: reprovado
Média entre 5.0 e 6.9: recuperação
Média 7.0 ou superior: aprovado"""

n1 = float(input("Enter the student's first grade: "))
n2 = float(input("Enter the student's second grade: "))

average = (n1 + n2) / 2

print(f"Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {average:.1f}")
if average < 5.0:
  print("O aluno está reprovado")
elif average >= 5.0 and average <= 6.9:
  print("O aluno está de recuperação")
elif average >= 7.0:
  print("O aluno está aprovado")