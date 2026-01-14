operator = str(input("Enter an operator: "))

n1 = 5
n2 = 10

match operator:
  case "+":
    result = n1 + n2
  case "-":
    result = n1 - n2
  case "*":
    result = n1 * n2
  case "/":
    result = n1 / n2
  case _:
    result = "Unsupported operator" 

print(result)