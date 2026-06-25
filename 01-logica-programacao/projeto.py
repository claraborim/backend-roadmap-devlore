while True:
    nome = (input("Digite seu nome: ")).strip()

    if nome.replace(" ", "").isalpha():
        break

    print("Insira um nome válido.")

while True:
    email = (input("Digite seu e-mail: ")).strip()

    if "@" in email and "." in email:
        break
    else:
        print("Insira um e-mail válido.")

while True:
    try:
        idade = int(input("Digite sua idade: "))

        if 0 <= idade <= 130:
            break

        print("Insira uma idade válida.")

    except ValueError:
        print("Insira uma idade válida.")

print("Cadastro realizado com sucesso.")