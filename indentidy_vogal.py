vogals = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def request(x):
  for i in vogals:
    if (x == i):
      return "É uma vogal"
  return "Não é uma vogal"

print(request("c"))
