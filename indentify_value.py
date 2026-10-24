import random

operator = ["+", "-", "*", "/"]

def entry_value(x, y, op):
  if (x == 0):
    return "Value is 0"
  elif ( y == 0):
    return "Value is 0"
  else:
    match op:
      case "+":
        res = x+y
        return res
      case "-":
        res = x-y
        return res
      case "*":
        res = x*y
        return res
      case "/":
        res = x/y
        return res

def checker(val):
    if (val == "Value is 0"):
      print("Impossível difivir por 0")
    elif (val % 2 == 0):
        print("é par")
        print(val)
    elif (val % 2 != 0):
        print("é impar")
        print(val)

def loop(rep, op):
  vetor = []

  choose_op = random.Random().randint(0, 3);
  for i in range(rep):
    x = random.Random().randint(1, 10)
    y = random.Random().randint(1, 10)
    vetor.append(entry_value(x, y, op[choose_op]))
  return vetor


print(loop(5, operator))
