# Crie um programa que recebe um número e imprime seu fatorial.

num = int(input("Digite um número: "))

if num < 0:
    print("Digite um número positivo.")
else:
    fatorial = 1

    for i in range(1, num + 1):
        fatorial *= i

    print(f"{num}! = {fatorial}")