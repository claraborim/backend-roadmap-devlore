# Dado uma lista de salários, calcule o total pago a todos os funcionários.

salarios = [2500, 900, 5000, 7500]
total = 0

for salario in salarios:
    total += salario

print(f"R$ {total:.2f}")