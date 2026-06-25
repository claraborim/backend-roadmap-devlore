# Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor aleatório gerado no início do programa seja chutado corretamente. O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa.

from random import randint

valor = randint(1, 10)

while True:
    try:
        chute = int(input("Chute um número de 1 a 10: "))

        if not 1 <= chute <= 10:
            print("Digite um número entre 1 e 10.")
            continue

        if chute == valor:
            print(f"Você acertou! O valor era: {valor}")
            break
        elif chute > valor:
            print("Quase! Você chutou acima do valor correto")
        else:
            print("Quase! Você chutou abaixo do valor correto")

    except ValueError:
        print("Digite apenas números inteiros.")