import re 
import random

print(re.search("[A-Z]","Senha"))
print(re.search("[A-Z]","seNha"))
print(re.search("[a-z]","seNha"))
print(re.search("[0-9]","seNha"))

numero_secreto = random.randint(1,200)
print(numero_secreto)