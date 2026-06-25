# Crie um gerenciador de login simples, com o máximo de 3 tentativas. Usuário: jhonatan Senha: senha123

usuario = ""
senha = ""

tentativas = 0

while (usuario != "jhonatan" and senha != "senha123") and tentativas < 3:
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    tentativas += 1

if usuario == "jhonatan" and senha == "senha123":
    print("Login feito com sucesso.")
else:
    print("Aguarde 30 minutos antes de tentar novamente.")