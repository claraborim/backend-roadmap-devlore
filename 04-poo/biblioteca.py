class Livro:
    def __init__(self, titulo: str, autor: str, isbn: str):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        return f"\n{'─' * 30}\nTítulo: {self.titulo}\nAutor:  {self.autor}\nISBN:   {self.isbn}"

class Biblioteca:
    def __init__(self):
        self.livros = []

    def cadastrar_livro (self, livro):
        self.livros.append(livro)

    def buscar_titulo (self, titulo):
        if len(self.livros) > 0:
            for livro in self.livros:
                if livro.titulo == titulo:
                    print(livro)
                    break
            else:
                print("\nLivro não encontrado.")
        else:
            print("\nA biblioteca está vazia.")

    def listar_livros(self):
        if len(self.livros) > 0:
            for livro in self.livros:
                print(livro)
        else:
            print("\nA biblioteca está vazia.")
    
biblioteca = Biblioteca()

while True:
    print("\n-=-=-=- MENU: BIBLIOTECA -=-=-=-\n"
        "1- Cadastrar livro\n"
        "2- Buscar por título\n"
        "3- Mostrar biblioteca\n"
        "4- Sair")

    opcao = input("Opção: ")

    match opcao:
        case "1":
            print()
            livro = Livro(input("Título: "), input("Autor: "), input("ISBN: "))
            biblioteca.cadastrar_livro(livro)
        case "2":
            print()
            titulo = input("Título a buscar: ")
            biblioteca.buscar_titulo(titulo)
            print(f"{'─' * 30}")
        case "3":
            biblioteca.listar_livros()
            print('─' * 30)
        case "4":
            break
        case _:
            print("\nOpção inválida.")