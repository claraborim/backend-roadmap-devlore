# Escreva um programa que retorne o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.

sal_mensal = float(input("Digite seu salário mensal: R$ "))
horas_mes = int(input("Digite quantas horas você trabalha no mês: "))

val_hora = sal_mensal / horas_mes

print(f"Seu valor/hora é: R$ {val_hora:.2f}")