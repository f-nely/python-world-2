"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado 
"""
housePrice = float(input("How much does the house cost? "))
salary = float(input("What is the buyer's salary? "))
years = int(input("How many years do you want the financing for? "))

mounthlyPayment = housePrice / (years * 12)
percentSalary = salary * 0.3

print(f"To purchase a house costing R${housePrice:.2f} over {years} years, the monthly payment will be R${mounthlyPayment:.2f}")
print(percentSalary)
if mounthlyPayment <= percentSalary:
  print("Loan approved!")
else:
  print("Loan denied!")