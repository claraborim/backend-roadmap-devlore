# Dados uma coleção de dados "idades" [15,46,75,34,23] imprima na tela a soma destes valores.

idades = [15,46,75,34,23]
soma = 0

for i in range (len(idades)):
    soma += idades[i]

print(soma)