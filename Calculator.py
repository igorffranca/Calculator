import os

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def clear():
    if os.name == 'nt':
      os.system('cls')
    else:
       os.system('clear')

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

def calculator():
  clear()
  print(logo)

  operators = {"+": add, "-": subtract, "*": multiply, "/": divide}
  flag = True
  
  num1 = float(input("What's the first number?: "))
  
  print()
  for operator in operators:
      print(operator)
  print()
  
  operator = input("Pick an operator from the line above: ")
  print()
  
  num2 = float(input("What's the second number?: "))
  print()
  
  first_answer = operators[operator](num1, num2)
  print(f"{num1} {operator} {num2} = {first_answer}")
  
  while flag:
    
    operator = input("Pick another operator: ")
    num3 = float(input("What's the next number?: "))
    second_answer = operators[operator](first_answer, num3)
    print(f"{first_answer} {operator} {num3} = {second_answer}")
  
    continue_calculation = input(f"\nType 'y' to continue calculating with {second_answer}, or type 'n' to start a new calculation: ").lower().strip()
    if continue_calculation == "y":
      first_answer = second_answer
    else:
      flag = False
      clear()
      calculator()

calculator()
