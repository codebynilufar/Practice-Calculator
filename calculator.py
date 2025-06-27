def add(a, b):
    return a + b

def substruct(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def validate_expression(expression: str) -> bool:
  
  split = expression.split()
  checkings = []
  checkings.append(len(split) == 3)
  checkings.append((split[1] in ("+", "-", "*", "/")))
  
  checkings = [True, True, False]
  
  return all(checkings)  


